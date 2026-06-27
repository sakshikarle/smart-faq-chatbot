const chatBox = document.getElementById("chat-box");
const input = document.getElementById("message");
const typing = document.getElementById("typing");

// ENTER KEY SEND
input.addEventListener("keypress", function (e) {
    if (e.key === "Enter") {
        sendMessage();
    }
});

// ADD MESSAGE (SAFE + IMAGE SUPPORT)
function addMessage(content, sender) {

    const message = document.createElement("div");
    message.className = "message " + sender;

    const icon = document.createElement("div");
    icon.className = "icon";
    icon.innerHTML = sender === "user" ? "🧑" : "🤖";

    const bubble = document.createElement("div");
    bubble.className = "text";

    // IMAGE CHECK (SAFE FIX)
    const isImage =
        typeof content === "string" &&
        (content.startsWith("http") ||
         content.includes(".jpg") ||
         content.includes(".png") ||
         content.includes(".jpeg") ||
         content.includes(".gif"));

    if (isImage && sender === "user") {
        bubble.innerHTML = `<img src="${content}" style="max-width:200px;border-radius:10px;">`;
    } else {
        bubble.innerText = content;
    }

    message.appendChild(icon);
    message.appendChild(bubble);

    chatBox.appendChild(message);
    chatBox.scrollTop = chatBox.scrollHeight;
}

// SEND MESSAGE
function sendMessage() {

    const msg = input.value.trim();
    if (msg === "") return;

    addMessage(msg, "user");
    input.value = "";

    typing.style.display = "block";

    fetch("/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: "message=" + encodeURIComponent(msg)
    })
    .then(res => res.text())
    .then(data => {

        typing.style.display = "none";

        setTimeout(() => {
            addMessage(data, "bot");
        }, 300);

    })
    .catch(() => {

        typing.style.display = "none";
        addMessage("❌ Server Error! Try again.", "bot");

    });
}

// CLEAR CHAT
function clearChat() {

    chatBox.innerHTML = `
        <div class="message bot">
            <div class="icon">🤖</div>
            <div class="text">
                Hello 👋<br>
                Welcome back to Smart FAQ Chatbot.<br>
                Ask me anything!
            </div>
        </div>
    `;
}