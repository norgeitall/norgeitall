<script>
	import '@evidence-dev/tailwind/fonts.css';
	import '../app.css';
	import { EvidenceDefaultLayout } from '@evidence-dev/core-components';
	export let data;
</script>

<EvidenceDefaultLayout {data} title="Dag 1" githubRepo="https://github.com/dag1-no/dag1">
	<slot slot="content" />
</EvidenceDefaultLayout>
