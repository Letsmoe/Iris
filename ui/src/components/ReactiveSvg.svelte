<script lang="ts">
	export let src: string;
	export let alt: string = "";
	export let width: number = 24;
	export let height: number = 24;
</script>

<img {src} {alt} class="dark:invert" {width} {height}>