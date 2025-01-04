<script lang="ts">
    import {onMount} from "svelte";
    import * as Card from "$lib/components/ui/card/index.ts";
    import MathJax from "$lib/components/MathJax.svelte";

    export let title: string;
    export let solution: string;
    export let author: string;
</script>

<Card.Root>
    <Card.Header>
        <Card.Title>{title}</Card.Title>
        <Card.Description>{(author === "") ? "AOPS" : author}</Card.Description>
    </Card.Header>
    <Card.Content class="space-y-3">
        {@const math = solution}
        <MathJax {math}></MathJax>
    </Card.Content>
</Card.Root>