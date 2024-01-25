function insertChar(char) {
  var result = document.getElementById("result");
  result.value += char;
}

function clearResult() {
  var result = document.getElementById("result");
  result.value = "";
}

function deleteChar() {
  var result = document.getElementById("result");
  result.value = result.value.slice(0, -1);
}

function calculate() {
  var result = document.getElementById("result");
  try {
    result.value = eval(result.value);
  } catch (error) {
    result.value = "Error";
  }
}
