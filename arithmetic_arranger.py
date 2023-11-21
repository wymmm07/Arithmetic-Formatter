def arithmetic_arranger(problems, show_answers=False):
  if len(problems) > 5:
    return "Error: Too many problems."

  arranged_problems = {"top": [], "bottom": [], "line": [], "answer": []}

  for problem in problems:
    operand1, operator, operand2 = problem.split()

    if not (operand1.isdigit() and operand2.isdigit()):
      return "Error: Numbers must only contain digits."

    if operator not in ['+', '-']:
      return "Error: Operator must be '+' or '-'."

    if len(operand1) > 4 or len(operand2) > 4:
      return "Error: Numbers cannot be more than four digits."

    max_length = max(len(operand1), len(operand2)) + 2
    arranged_problems["top"].append(operand1.rjust(max_length))
    arranged_problems["bottom"].append(operator +
                                       operand2.rjust(max_length - 1))
    arranged_problems["line"].append('-' * max_length)

    if show_answers:
      if operator == '+':
        answer = str(int(operand1) + int(operand2))
      else:
        answer = str(int(operand1) - int(operand2))
      arranged_problems["answer"].append(answer.rjust(max_length))

  lines = [
      "    ".join(arranged_problems["top"]),
      "    ".join(arranged_problems["bottom"]),
      "    ".join(arranged_problems["line"]),
  ]

  if show_answers:
    lines.append("    ".join(arranged_problems["answer"]))

  return "\n".join(lines)


# Example usage:
problems = ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]
print(arithmetic_arranger(problems, True))
