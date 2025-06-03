<script>
  export let text = 'This is where the output will go';
</script>

<div class="output-panel">
  <div class="output-content">
    {@html text}
  </div>
</div>

<style>
  .output-panel {
    flex: 1;
    overflow-y: auto;
    padding: 1rem;
    background: #e8f0fe;
    border-top: 1px solid #ddd;
    border-bottom: 1px solid #ddd;
    white-space: pre-wrap;
  }

  .output-content {
    white-space: pre-wrap; /* Preserve line breaks */
  }
</style>
