<script lang="ts">
	import { Cube } from 'radix-svelte-icons';
	import { DeviceStatus, DeviceType } from '../types';

	export let name: string;
	export let tags: string[];
	export let type: DeviceType;
	export let status: DeviceStatus;
</script>

<div class="flex flex-row items-center gap-2">
	<div class="rounded-full p-1.5"
	class:bg-green-400={status == DeviceStatus.ONLINE}
	class:bg-red-400={status == DeviceStatus.OFFLINE}
	class:bg-gray-400={status == DeviceStatus.UNKNOWN}>
		<!-- TODO: Add Device Type specific icon -->
		<Cube width={18} height={18} class="text-black"></Cube>
	</div>
	<span class="text-xs text-base-content">{name}</span>
	<div class="ml-auto flex flex-wrap gap-2">
		{#each tags as tag}
		<span class="badge badge-xs badge-neutral py-2 px-2 ml-auto">{tag}</span>
		{/each}
	</div>
</div>