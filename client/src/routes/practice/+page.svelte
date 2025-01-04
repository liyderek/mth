<script lang="ts">
    import * as Resizable from "$lib/components/ui/resizable/index.ts";
    import {Slider} from "$lib/components/ui/slider/index.js";
    import {Button} from "$lib/components/ui/button";
    import {buttonVariants} from "$lib/components/ui/button/index.ts";
    import * as Card from "$lib/components/ui/card/index.ts";
    import * as InputOTP from "$lib/components/ui/input-otp/index.ts";
    import * as AlertDialog from "$lib/components/ui/alert-dialog/index.ts";
    import Solutions from "$lib/components/Solutions.svelte"

    import {onMount} from "svelte";
    import {REGEXP_ONLY_DIGITS} from "bits-ui";

    let value = $state([10, 13]);

    let cur_year = $state(0);
    let cur_contest = $state("I");
    let cur_num = $state(0);

    let verdict = $state(0);
    let answer = $state("");

    let content = $state("");

    let open = $state(false);

    async function fetchRandom() {
        let response = await fetch(`http://localhost:5000/api/problems/AIME/random?min=${value[0]}&max=${value[1]}`);
        let problem = await response.json();
        cur_year = problem["year"];
        cur_contest = problem["contest"];
        cur_num = problem["num"];
        verdict = 0;
        answer = "";

        response = await fetch(`http://localhost:5000/api/problems/AIME/single?year=${cur_year}&contest=${cur_contest}&num=${cur_num}`);
        content = await response.text();
    }

    async function getVerdict() {
        const response = await fetch(`http://localhost:5000/api/problems/AIME/check?year=${cur_year}&contest=${cur_contest}&num=${cur_num}&answer=${answer}`);
        verdict = (await response.json())["verdict"] ? 1 : 2;
    }

    function getHTML(verdict: Number) {
        switch (verdict) {
            case 0:
                return "";
            case 1:
                return "<p class='text-green-300'>Correct</p>";
            case 2:
                return "<p class='text-red-400'>Wrong</p>";
            default:
                return "Unknown";
        }
    }

    onMount(async () => {
        await fetchRandom();
    });
</script>

<Resizable.PaneGroup direction="horizontal" class="min-h-screen">
    <Resizable.Pane defaultSize={83} class="flex justify-center">

        <div class="w-1/2 space-y-3 py-[12%]">
            <Card.Root>
                <Card.Header>
                    <Card.Title>n{cur_num}</Card.Title>
                    <Card.Description>AIME</Card.Description>
                </Card.Header>
                <Card.Content class="space-y-3">
                    {@html content}

                    <div class="align-middle flex relative">
                        <div class="inline-block my-auto">
                            <InputOTP.Root disabled={verdict === 1} maxlength={3} pattern={REGEXP_ONLY_DIGITS}
                                           bind:value={answer}
                                           onkeydown={(event) => {if (event.key === "Enter") getVerdict()}}>
                                {#snippet children({cells})}
                                    <InputOTP.Group>
                                        {#each cells as cell}
                                            <InputOTP.Slot {cell}/>
                                        {/each}
                                    </InputOTP.Group>
                                {/snippet}
                            </InputOTP.Root>
                        </div>
                        {#if verdict !== 1}
                            <div class="inline-block my-auto mx-2">
                                {@html getHTML(verdict)}
                            </div>
                        {/if}
                        {#if verdict === 1}
                            <div class="inline-block my-auto mx-2">
                                <Button variant="ghost" class="text-green-300" onclick={fetchRandom}>Next</Button>
                            </div>
                        {/if}
                        <!--                        <Button variant="outline" class="absolute top-0 right-0" onclick={fetchRandom}>skip</Button>-->
                        {#if verdict !== 1}
                            <AlertDialog.Root bind:open>
                                <AlertDialog.Trigger
                                        class={buttonVariants({ variant: "outline" }) + " absolute top-0 right-0"}>
                                    skip
                                </AlertDialog.Trigger>
                                <AlertDialog.Content>
                                    <AlertDialog.Header>
                                        <AlertDialog.Title>Are you absolutely sure?</AlertDialog.Title>
                                        <AlertDialog.Description>
                                            Skipping a problem is not recommended.
                                        </AlertDialog.Description>
                                    </AlertDialog.Header>
                                    <AlertDialog.Footer>
                                        <AlertDialog.Cancel>Cancel</AlertDialog.Cancel>
                                        <AlertDialog.Action onclick={() => {fetchRandom(); open = false;}}>Continue
                                        </AlertDialog.Action>
                                    </AlertDialog.Footer>
                                </AlertDialog.Content>
                            </AlertDialog.Root>
                        {/if}
                    </div>
                </Card.Content>
            </Card.Root>
            {#if verdict === 1}
                <Solutions year={cur_year} contest={cur_contest} num={cur_num}></Solutions>
            {/if}
        </div>

    </Resizable.Pane>
    <Resizable.Handle/>
    <Resizable.Pane class="m-2 space-y-1">
        <h1 class="text-xl">settings</h1>
        <p>Difficulty: {value[0]}-{value[1]}</p>
        <Slider type="multiple" bind:value min={1} max={15} step={1} class="max-w-72"/>
        <br>
        <Button variant="secondary">update</Button>
    </Resizable.Pane>
</Resizable.PaneGroup>