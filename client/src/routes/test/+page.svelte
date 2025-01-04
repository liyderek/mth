<script>
    import MathJax from '$lib/components/MathJax.svelte';
    import {Button} from "$lib/components/ui/button";
    import ProblemSolution from "$lib/components/ProblemSolution.svelte";
    import {onMount} from "svelte";

    let solutions = [{
        "title": "",
        "author": "",
        "content": ""
    }];

    async function fetchSolutions() {
        solutions.pop();
        let response = await fetch(`http://localhost:5000/api/problems/AIME/solution?year=2024&contest=II&num=15`);
        solutions = (await response.json())["solutions"];
    }

    onMount(async () => {
        await fetchSolutions();
    });
</script>

<div class="flex items-center justify-center">
    <div class="m-2 space-y-3 w-1/2 leading-8">
        <br>
        <br>
        {#each solutions as solution, index}
            <ProblemSolution title={solution["title"]} author={solution["author"]}
                             solution={solution["content"]}></ProblemSolution>
            <!--        <ProblemSolution title="Solution 1" solution={math}></ProblemSolution>-->
        {/each}
    </div>
</div>
<!--{@render "<MathJax {math}></MathJax"}-->
