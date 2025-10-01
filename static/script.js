// DOM Elements
const chatContainer = document.getElementById('chatContainer');
const userInput = document.getElementById('userInput');

// Add event listener for Enter key
userInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

// Function to add a message to the chat
function addMessage(message, isUser = false) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${isUser ? 'user-message' : 'bot-message'}`;
    messageDiv.textContent = message;
    chatContainer.appendChild(messageDiv);
    
    // Auto scroll to bottom
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

// Function to send message to backend
async function sendMessage() {
    const message = userInput.value.trim();
    
    if (message === '') return;

    // Add user message to chat
    addMessage(message, true);
    
    // Clear input
    userInput.value = '';
    
    try {
        // Send message to backend
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `message=${encodeURIComponent(message)}`
        });
        
        const data = await response.json();
        
        // Add bot response to chat
        addMessage(data.reply);
        
    } catch (error) {
        console.error('Error:', error);
        addMessage('Sorry, there was an error processing your request. Please try again.');
    }
}

// Add welcome message when page loads
window.onload = function() {
    addMessage("Hello! I'm Crypto Buddy. Ask me about cryptocurrency prices, trading info, or news!");
};