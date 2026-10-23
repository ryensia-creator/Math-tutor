import ipywidgets as widgets
from IPython.display import display


class Equation:

  def __init__(self, equation_str):
    self.raw_input = equation_str.replace(" ", "").lower()
    if "=" not in self.raw_input or self.raw_input.count("=") != 1:
      self.left_x = self.left_c = self.right_x = self.right_c = 0
      self.leftequation = self.rightequation = "0"
      return
    left, right = self.raw_input.split("=")
    self.left_x, self.left_c = self.extract_coefficients(left)
    self.right_x, self.right_c = self.extract_coefficients(right)
    self.updatetext()

  def extract_coefficients(self, side_str):
    if not side_str:
      return 0.0, 0.0
    try:
      s = side_str
      if s.startswith("x"):
        s = "1*" + s
      elif s.startswith("+x"):
        s = "+1*" + s
      elif s.startswith("-x"):
        s = "-1*" + s
      python_friendly = (
          s.replace("x", "*x").replace("+*", "+").replace("-*", "-")
      )
      if python_friendly.startswith("*"):
        python_friendly = python_friendly[1:]
      result = eval(python_friendly, {"__builtins__": None}, {"x": 1j})
      if not isinstance(result, complex):
        result = complex(result)
      return float(result.imag), float(result.real)
    except Exception:
      return 0.0, 0.0

  def updatetext(self):

    def build_display(x, c):
      parts = []
      if x == 1:
        parts.append("x")
      elif x == -1:
        parts.append("-x")
      elif x != 0:
        parts.append(f"{int(x) if x.is_integer() else x}x")
      if c != 0:
        val = int(c) if c.is_integer() else c
        if parts:
          parts.append(f"+ {val}" if val > 0 else f"- {abs(val)}")
        else:
          parts.append(str(val))
      return " ".join(parts) if parts else "0"

    self.leftequation = build_display(self.left_x, self.left_c)
    self.rightequation = build_display(self.right_x, self.right_c)

  def __str__(self):
    return f"{self.leftequation} = {self.rightequation}"

  def solve_step(self):
    if self.right_x != 0:
      explanation = (
          f"Moving variable component ({self.right_x}x) to the Left Hand Side..."
      )
      self.left_x -= self.right_x
      self.right_x = 0
      self.updatetext()
      return True, explanation
    if self.left_x == 0:
      if self.left_c == self.right_c:
        explanation = "Identity equation detected! Infinite solutions."
      else:
        explanation = "Contradiction detected! No solution."
      return False, explanation
    if self.left_c != 0:
      explanation = (
          f"Moving constant value ({self.left_c}) to the Right Hand Side..."
      )
      self.right_c -= self.left_c
      self.left_c = 0
      self.updatetext()
      return True, explanation
    if self.left_x != 1:
      divisor = int(self.left_x) if self.left_x.is_integer() else self.left_x
      explanation = f"Isolating x, dividing both sides by {divisor}:"
      raw_result = self.right_c / self.left_x
      self.left_x = 1
      if raw_result.is_integer():
        self.right_c = float(int(raw_result))
        self.updatetext()
      else:
        self.right_c = raw_result
        rounded = round(raw_result, 2)
        self.leftequation = "x"
        self.rightequation = f"{raw_result:.5f} (rounded to {rounded})"
      return True, explanation
    return False, "Equation is fully solved!"


# --- ALL-WIDGET INTERFACE INTERACTIVE SETUP ---
current_equation = None

# Input and control widgets
input_text = widgets.Text(value="", description="Equation:", placeholder="e.g., 3x + 5 = x - 7")
load_btn = widgets.Button(description="Load Equation", button_style="info")
next_btn = widgets.Button(description="Next Step", button_style="success", disabled=True)
reset_btn = widgets.Button(description="Reset", button_style="warning")

# Output display widgets (replacing print statements entirely)
status_label = widgets.HTML(value="<b>Status:</b> Awaiting equation input...")
equation_label = widgets.HTML(value="<h3>Current State: </h3>")
log_area = widgets.HTML(value="<b>Steps Log:</b><br>", layout=widgets.Layout(min_height="100px"))

# Layout Setup
controls_box = widgets.HBox([input_text, load_btn])
action_box = widgets.HBox([next_btn, reset_btn])
display_box = widgets.VBox([status_label, equation_label, log_area], layout=widgets.Layout(margin="10px 0px 0px 0px"))
main_container = widgets.VBox([controls_box, action_box, display_box])


def load(b):
  global current_equation, steps_log
  current_equation = Equation(input_text.value)
  next_btn.disabled = False
  status_label.value = "<b style='color: green;'>Status:</b> Equation Loaded successfully."
  equation_label.value = f"<h3>Current State: <span style='color: blue;'>{current_equation}</span></h3>"
  steps_log = ["<b>Steps Log:</b>"]
  log_area.value = "<br>".join(steps_log)


def next_step(b):
  global current_equation, steps_log
  if current_equation is None:
    return

  has_next_step, explanation = current_equation.solve_step()
  steps_log.append(f"• {explanation}")
  log_area.value = "<br>".join(steps_log)
  equation_label.value = f"<h3>Current State: <span style='color: blue;'>{current_equation}</span></h3>"

  if not has_next_step:
    status_label.value = "<b style='color: darkgreen;'>Status:</b> Completed!"
    next_btn.disabled = True


def reset_session(b):
  global current_equation
  current_equation = None
  next_btn.disabled = True
  input_text.value = ""
  status_label.value = "<b>Status:</b> Session reset. Awaiting equation input..."
  equation_label.value = "<h3>Current State: </h3>"
  log_area.value = "<b>Steps Log:</b><br>"


load_btn.on_click(load)
next_btn.on_click(next_step)
reset_btn.on_click(reset_session)

# Render everything
display(main_container)
