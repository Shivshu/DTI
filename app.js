const messages = document.getElementById("messages");

const userInput = document.getElementById("user-input");

const sendButton = document.getElementById("send-button");

const voiceInput = document.getElementById("voice-input");

// Speech recognition setup
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

const recognition = new SpeechRecognition();

recognition.lang = 'en-US';

recognition.interimResults = false;


// Event listener for voice input button
voiceInput.addEventListener("click", () => {
    recognition.start();
});


// Event listener for send button
sendButton.addEventListener("click", () => {
    sendMessage();
});


// Event listener for Enter key
userInput.addEventListener("keyup", (event) => {
    if (event.key === "Enter") {
        sendMessage();
    }
});


// Function to handle sending message
function sendMessage() {
    const userMessage = document.createElement("div");
    userMessage.classList.add("message", "user-message");
    const messageBox = document.createElement("div");
    messageBox.classList.add("message-box");
    messageBox.textContent = userInput.value;
    userMessage.appendChild(messageBox);
    messages.appendChild(userMessage);
    userInput.value = "";


    // Add chatbot response
    setTimeout(() => {
        const chatbotMessage = document.createElement("div");
        chatbotMessage.classList.add("message", "chatbot-message");
        const messageBox = document.createElement("div");
        messageBox.classList.add("message-box");
        messageBox.textContent = "Hello, I'm ChatterBot!";
        chatbotMessage.appendChild(messageBox);
        messages.appendChild(chatbotMessage);
        messages.scrollTop = messages.scrollHeight; // Scroll to bottom
    }, 1000);
}


// Event listener for speech recognition results
recognition.addEventListener('result', (event) => {
    const transcript = Array.from(event.results)
        .map(result => result[0].transcript)
        .join('');
    
    userInput.value = transcript;
});



// Event listener for end of speech recognition
recognition.addEventListener('end', () => {
    
    // Automatically trigger sending the message after speech recognition ends
    sendMessage();
});
