<script lang="ts">
	import Counter from './Counter.svelte';
	import Textbox from './Textbox.svelte';
	import welcome from '$lib/images/svelte-welcome.webp';
	import welcomeFallback from '$lib/images/svelte-welcome.png';
	import { API_BASE_URL } from "$lib/constants";

	const { data } = $props();
	let stuff = [ {a:"a"}, {a:"b"}, {a:"c"} ];

	async function handleEnterText(text:string) {
		const response = await fetch(API_BASE_URL + '/query', {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify({ text: text }),
		});
		const data = await response.json();
		return data;
	}
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section>
	<h1>
		<span class="welcome">
			<picture>
				<source srcset={welcome} type="image/webp" />
				<img src={welcomeFallback} alt="Welcome" />
			</picture>
		</span>

		to your new<br />SvelteKit app
	</h1>

	<div>{JSON.stringify(data)}</div>

	{#each data.posts as post}
		<p>ITEM!: {post.item_id}</p>
	{/each}

	<h2>
		try editing <strong>src/routes/+page.svelte</strong>
	</h2>

	<Textbox enterText={handleEnterText}/>

	<Counter />
</section>

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 0.6;
	}

	h1 {
		width: 100%;
	}

	.welcome {
		display: block;
		position: relative;
		width: 100%;
		height: 0;
		padding: 0 0 calc(100% * 495 / 2048) 0;
	}

	.welcome img {
		position: absolute;
		width: 100%;
		height: 100%;
		top: 0;
		display: block;
	}
	
</style>
