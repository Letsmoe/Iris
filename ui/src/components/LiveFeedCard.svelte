<script lang="ts">
	export let src: string;
	export let type: HTMLSourceElement["type"];
	export let name: string;
</script>

<div class="card border border-base-300 p-0 rounded-lg relative">
	<video class="w-full h-full my-0 rounded-lg" controls>
		<source {src} {type}>
		Your browser does not support the video tag.
		<track kind="captions">
	</video>
	<div class="absolute left-4 top-4 bg-opacity-30 bg-black px-2.5 py-0.5 rounded-full flex flex-row gap-2 text-sm">
		<span class="text-green-400">• Live</span>
		|
		<span>{name}</span>
	</div>
</div>

