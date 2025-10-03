import base64

def get_svg_as_data_uri(svg_path):
    """Convert SVG file to base64 data URI"""
    try:
        with open(svg_path, 'r', encoding='utf-8') as file:
            svg_content = file.read()
        b64_encoded = base64.b64encode(svg_content.encode('utf-8')).decode('utf-8')
        return f"data:image/svg+xml;base64,{b64_encoded}"
    except FileNotFoundError:
        print(f"SVG file not found: {svg_path}")
        return None

bot_logo = get_svg_as_data_uri('public/logo.svg') 
user_logo = get_svg_as_data_uri('public/user.svg')  
css = '''
<style>
.chat-container {
    max-height: 600px;
    overflow-y: auto;
    padding: 1rem;
    background-color: #1e1e1e;
    border-radius: 0.5rem;
    scroll-behavior: smooth;
}
.chat-message {
    padding: 1.5rem; 
    border-radius: 0.5rem; 
    margin-bottom: 1rem; 
    display: flex;
    animation: fadeIn 0.3s ease-in;
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
    width: 20%;
}
.chat-message .avatar img {
    max-width: 78px;
    max-height: 78px;
    border-radius: 50%;
    object-fit: cover;
}
.chat-message .message {
    width: 80%;
    padding: 0 1.5rem;
    color: #fff;
}
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}
/* Scroll anchor for auto-scroll functionality */
.scroll-anchor {
    height: 1px;
    width: 1px;
}
</style>
'''
js_auto_scroll = '''
<script>
let chatContainer;
let shouldAutoScroll = true;
let isAtBottom = true;
function initializeChat() {
    chatContainer = document.getElementById('chat-container');
    if (!chatContainer) return;
    // Scroll to bottom initially
    scrollToBottom();
    // Listen for scroll events to detect if user scrolled up
    chatContainer.addEventListener('scroll', handleScroll);
}
function handleScroll() {
    const threshold = 100; // pixels from bottom
    isAtBottom = chatContainer.scrollTop + chatContainer.clientHeight >= 
                 chatContainer.scrollHeight - threshold;
    
    // Only auto-scroll if user is near the bottom
    shouldAutoScroll = isAtBottom;
}
function scrollToBottom(smooth = true) {
    if (!chatContainer) return; 
    const scrollOptions = {
        top: chatContainer.scrollHeight,
        behavior: smooth ? 'smooth' : 'instant'
    };
    chatContainer.scrollTo(scrollOptions);
}
function addMessage(messageHtml) {
    if (!chatContainer) return;
    // Check if we should auto-scroll before adding the message
    const wasAtBottom = shouldAutoScroll;
    // Add the new message
    chatContainer.insertAdjacentHTML('beforeend', messageHtml);
    // Auto-scroll if user was at bottom or this is the first message
    if (wasAtBottom || chatContainer.children.length === 1) {
        setTimeout(() => scrollToBottom(true), 100);
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', initializeChat);
// Alternative initialization for dynamic loading
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeChat);
} else {
    initializeChat();
}
</script>
'''
chat_container_start = '''
<div id="chat-container" class="chat-container">
'''
chat_container_end = '''
    <div class="scroll-anchor"></div>
</div>
'''
bot_template = f'''
<div class="chat-message bot">
    <div class="avatar">
        <img src="{bot_logo}" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{{{MSG}}}}</div>
</div>
'''
user_template = f'''
<div class="chat-message user">
    <div class="avatar">
        <img src="{user_logo}">
    </div>    
    <div class="message">{{{{MSG}}}}</div>
</div>
'''
def create_chat_interface():
    """Create the complete chat interface with auto-scroll"""
    return f"""
    {css}
    {js_auto_scroll}
    {chat_container_start}
    <!-- Messages will be inserted here -->
    {chat_container_end}
    """
def add_new_message_js(message_html):
    """JavaScript to add a new message with auto-scroll"""
    escaped_html = message_html.replace('"', '\\"').replace('\n', '\\n')
    return f'addMessage("{escaped_html}");'
