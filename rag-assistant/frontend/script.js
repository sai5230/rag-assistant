function sendMessage() {
  const msg = document.getElementById("question").value;

  fetch("http://localhost:8000/api/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      message: msg,
      sessionId: "test"
    })
  })
  .then(response => {
    if (!response.ok) {
      throw new Error("HTTP error " + response.status);
    }
    return response.json();
  })
  .then(data => {
    document.getElementById("response").innerText = data.answer;
  })
  .catch(error => {
    alert("ERROR: " + error.message);
    console.error(error);
  });
}