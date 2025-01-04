<script lang="ts">
    import MathJax from '$lib/components/MathJax.svelte';
    import {Button} from "$lib/components/ui/button";
    import ProblemSolution from "$lib/components/ProblemSolution.svelte";
    import {onMount} from "svelte";

    export let year: number;
    export let contest: string;
    export let num: number;

    let solutions = [{
        "title": "",
        "author": "",
        "content": ""
    }];

    async function fetchSolutions() {
        solutions.pop();
        let response = await fetch(`http://localhost:5000/api/problems/AIME/solution?year=${year}&contest=${contest}&num=${num}`);
        solutions = (await response.json())["solutions"];
        console.log(solutions);
    }

    onMount(async () => {
        await fetchSolutions();
    });
</script>

{#each solutions as solution, index}
    <ProblemSolution title={solution["title"]} author={solution["author"]}
                     solution={solution["content"]}></ProblemSolution>
    <!--        <ProblemSolution title="Solution 1" solution={math}></ProblemSolution>-->
{/each}
<!--{@render "<MathJax {math}></MathJax"}-->
