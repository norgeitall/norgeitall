<script>
	import '@evidence-dev/tailwind/fonts.css';
	import '../app.css';
	import { EvidenceDefaultLayout } from '@evidence-dev/core-components';
	export let data;
</script>

<EvidenceDefaultLayout {data} title="Norge i tall" githubRepo="https://github.com/norgeitall/norgeitall">
	<slot slot="content" />
</EvidenceDefaultLayout>
