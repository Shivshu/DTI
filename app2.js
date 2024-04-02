const messages = document.getElementById("messages");
const userInput = document.getElementById("user-input");
const sendButton = document.getElementById("send-button");
const voiceInput = document.getElementById("voice-input");

// Function to handle sending message
function sendMessage(message) {
    const userMessage = document.createElement("div");
    userMessage.classList.add("message", "user-message");
    const messageBox = document.createElement("div");
    messageBox.classList.add("message-box");
    messageBox.textContent = message;
    userMessage.appendChild(messageBox);
    messages.appendChild(userMessage);
    userInput.value = "";

    // Automatically scroll to the bottom of the messages
    messages.scrollTop = messages.scrollHeight;

    // Call ChatGPT to generate a response
    getChatGPTResponse(message);
}

// Function to handle receiving ChatGPT's response
function receiveMessage(message) {
    const chatbotMessage = document.createElement("div");
    chatbotMessage.classList.add("message", "chatbot-message");
    const messageBox = document.createElement("div");
    messageBox.classList.add("message-box");
    messageBox.textContent = message;
    chatbotMessage.appendChild(messageBox);
    messages.appendChild(chatbotMessage);

    // Automatically scroll to the bottom of the messages
    messages.scrollTop = messages.scrollHeight;
}

// Event listener for voice input button
voiceInput.addEventListener("click", () => {
    // Start speech recognition
    recognition.start();
});

// Event listener for send button
sendButton.addEventListener("click", () => {
    // Get user input
    const message = userInput.value.trim();
    if (message !== "") {
        sendMessage(message);
    }
});

// Event listener for Enter key
userInput.addEventListener("keyup", (event) => {
    if (event.key === "Enter") {
        // Get user input
        const message = userInput.value.trim();
        if (message !== "") {
            sendMessage(message);
        }
    }
});

// Function to call ChatGPT API
async function getChatGPTResponse(input) {
    try {
        const response = await fetch("https://api.openai.com/v1/completions", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Authorization": "Bearer YOUR_API_KEY"
            },
            body: JSON.stringify({
                prompt: input,
                max_tokens: 50,
                temperature: 0.7
            })
        });
        const data = await response.json();
        const chatGPTResponse = data.choices[0].text.trim();
        receiveMessage(chatGPTResponse);
    } catch (error) {
        console.error("Error:", error);
        receiveMessage("Sorry, I couldn't understand that.");
    }
}
