<script lang="ts">
  import { tick } from 'svelte';

  let { text = $bindable(), enterText = $bindable() as (t: string) => void } = $props();

  function handleEnterText(t: string) {
    if (t.trim() === '') {
      console.warn('Attempted to send empty message');
      return; // Prevent sending empty messages
    }
    enterText(t);
    text = '';
    console.log('Sending text:', t);
  }
</script>

<div class="input-panel">
  <textarea
    placeholder="Type your message…"
    bind:value={text}
    rows="1"
    class="chat-input"
    onkeydown={(e) => {
      if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        handleEnterText(text);
      }
    }}
  ></textarea>
  <button class="send-button" onclick={() => handleEnterText(text)}>Send</button>
</div>

<style>
  .input-panel {
    display: flex;
    padding: 0.5rem 1rem;
    background: #ffffff;
  }

  .chat-input {
    flex: 1;
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 0.4rem;
    margin-right: 0.5rem;
    font-size: 1rem;
  }

  textarea {
    flex: 1;
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 0.25rem;
    resize: vertical; /* allows manual resizing */
    max-height: 200px;
    overflow-y: auto; /* show scrollbar if content exceeds max-height */
  }

  .send-button {
    padding: 0.5rem 1rem;
    background: #007aff;
    color: white;
    border: none;
    border-radius: 0.4rem;
    cursor: pointer;
    font-size: 1rem;
  }

  .send-button:hover {
    background: #005fcc;
  }
</style>
