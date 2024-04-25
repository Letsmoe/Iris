<script lang="ts">
	export let header: string;
</script>

<div class="card border border-base-300 rounded-lg">
	<div class="card-title px-2 py-2 border-b border-b-base-300 bg-base-300 rounded-t-lg">
		<span class="text-base-content">{header}</span>
	</div>
	<div class="p-2 bg-base-200 h-full overflow-auto">
		<slot />
	</div>
</div>