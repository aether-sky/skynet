<script lang="ts">
  import Textbox from './Textbox.svelte';
  import OutputFrame from './OutputFrame.svelte';
  import { API_BASE_URL } from '$lib/constants';

  const { data } = $props();

  let text = $state('');
  let selectedModel = $state(data.models?.[0]?.id || '1'); // Use first model as default

  async function handleEnterText(text: string) {
    const response = await fetch(API_BASE_URL + '/query', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: text }),
    });
    text = '';
    const data = await response.json();
    return data;
  }
</script>

<svelte:head>
  <title>Skynet AI Demo Site</title>
  <meta name="description" content="Skynet AI Demo Site" />
</svelte:head>

<div class="container">
  <div class="header">
    <div>
      <select class="model-dropdown" bind:value={selectedModel}>
        {#each data.models as model}
          <option value={model.id}>{model.name}</option>
        {/each}
      </select>
    </div>
    <a
      href="https://github.com/aether-sky/skynet"
      target="_blank"
      rel="noopener"
      class="github-link"
      aria-label="GitHub"
    >
      <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" class="icon" viewBox="0 0 24 24">
        <path
          d="M12 .297c-6.6 0-12 5.4-12 12 0 5.3 3.4 9.8 8 11.4.6.1.8-.3.8-.6v-2.3c-3.2.7-3.9-1.6-3.9-1.6-.6-1.6-1.5-2-1.5-2-1.2-.9.1-.9.1-.9 1.3.1 2 .9 2 .9 1.1 2 2.9 1.5 3.6 1.2.1-.8.4-1.5.8-1.9-2.6-.3-5.3-1.3-5.3-5.8 0-1.3.5-2.4 1.3-3.3-.1-.3-.6-1.5.1-3.1 0 0 1-.3 3.3 1.3.9-.3 1.9-.4 2.9-.4 1 0 2 .1 2.9.4 2.3-1.6 3.3-1.3 3.3-1.3.7 1.6.2 2.8.1 3.1.8.9 1.3 2 1.3 3.3 0 4.5-2.7 5.5-5.3 5.8.4.4.8 1.2.8 2.3v3.4c0 .3.2.7.8.6 4.6-1.6 8-6 8-11.4 0-6.6-5.4-12-12-12z"
        />
      </svg>
    </a>
  </div>
  <div class="content-area">
    {#if false}
      {#each data.posts as post}
        <p>ITEM!: {post.item_id}</p>
      {/each}
    {/if}

    <OutputFrame />

    <Textbox bind:text enterText={handleEnterText} />
  </div>
</div>

<style>
  :global(body) {
    margin: 0;
    font-family: system-ui, sans-serif;
    background-color: #f9f9f9;
  }

  .container {
    display: flex;
    flex-direction: column;
    height: 100vh;
    width: 100vw;
    background-color: #f9f9f9;
  }

  .header {
    display: flex;
    flex-shrink: 0;
    align-items: center;
    justify-content: space-between;
    padding: 0.5rem 1rem;
    background-color: #ffffff;
    box-shadow: 0 1px 4px rgba(0, 0, 0, 0.1);
  }

  .content-area {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: 100%;
    margin: 0 auto;
    gap: 1rem;
  }
  .content-area > :global(*) {
    width: 100%;
  }

  .model-dropdown {
    font-size: 0.9rem;
    padding: 0.3rem 0.5rem;
  }

  .github-link {
    color: #333;
    text-decoration: none;
  }

  .github-link .icon {
    width: 1.2rem;
    height: 1.2rem;
  }
</style>
