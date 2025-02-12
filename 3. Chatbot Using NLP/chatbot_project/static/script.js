document.getElementById("send").addEventListener("click", async () => {
  const messageInput = document.getElementById("message");
  const message = messageInput.value.trim();

  if (!message) {
    alert("Please enter a message.");
    return;
  }

  try {
    // Send message to the backend
    const response = await fetch("http://127.0.0.1:5000/chat", {  // Update this URL
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message }),
    });

    // Check if the response is OK (status code 200-299)
    if (!response.ok) {
      throw new Error(`Server returned ${response.status}: ${response.statusText}`);
    }

    // Parse the JSON response
    const data = await response.json();

    // Display user and bot messages
    const chatDiv = document.getElementById("chat");
    chatDiv.innerHTML += `<p><strong>You:</strong> ${message}</p>`;
    chatDiv.innerHTML += `<p><strong>Bot:</strong> ${data.response}</p>`;
    chatDiv.scrollTop = chatDiv.scrollHeight; // Auto-scroll to the latest message
  } catch (error) {
    console.error("Error:", error);
    alert("An error occurred. Please try again.");
  }

  // Clear the input field
  messageInput.value = "";
});