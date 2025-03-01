<script>
	import '@evidence-dev/tailwind/fonts.css';
	import '../app.css';
	import { EvidenceDefaultLayout } from '@evidence-dev/core-components';
	export let data;
	const env = import.meta.env;
</script>

<EvidenceDefaultLayout {data} title="Norge i tall" githubRepo="https://github.com/norgeitall/norgeitall">
	<slot slot="content" />
</EvidenceDefaultLayout>

{#if env.PROD}
	<script
		data-goatcounter="https://norgeitall.goatcounter.com/count"
		async
		src="//gc.zgo.at/count.js"
	></script>
{/if}
