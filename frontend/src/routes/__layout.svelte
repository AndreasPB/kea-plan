<script>
  import Navbar from "../components/navbar.svelte"
</script>

<div class="flex flex-col h-screen justify-between">
  <Navbar />
  <div class="mb-auto container mx-auto">
    <slot />
  </div>
</div>
