<script lang="ts">
	import { tick } from "svelte";


	let { text, enterText = $bindable() as (t: string) => void } = $props();


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

<div class="textbox">
	<textarea
		placeholder="Type your message…"
		bind:value={text}
		rows="1"
		onkeydown={(e) => {
			if (e.key === 'Enter' && !e.shiftKey) {
				e.preventDefault();
				handleEnterText(text);
			}
		}}
	></textarea>
	<button onclick={() => handleEnterText(text)}>Send</button>
</div>

<style>
	.textbox {
		display: flex;
		gap: 0.5rem;
		align-items: flex-start;
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

	button {
		padding: 0.5rem 1rem;
		background: #007bff;
		color: white;
		border: none;
		border-radius: 0.25rem;
		cursor: pointer;
		height: fit-content;
	}

	button:hover {
		background: #0056b3;
	}
</style>
