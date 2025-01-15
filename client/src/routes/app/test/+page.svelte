<script lang="ts">
    import {onMount} from "svelte";
    import {Button} from "$lib/components/ui/button";
    import * as Resizable from "$lib/components/ui/resizable";
    import * as Card from "$lib/components/ui/card";
    import * as InputOTP from "$lib/components/ui/input-otp";
    import {REGEXP_ONLY_DIGITS} from "bits-ui";

    let content: string[] = [];

    onMount(async () => {
        content = await fetchContent();
        console.log(content);
    });

    const fetchContent = (async () => {
        const response = await fetch("http://localhost:5000/api/problems/AIME/test?year=2024&contest=I");
        return (await response.json())["problems"];
    });

    async function getVerdict(index: number) {
        const response = await fetch(`http://localhost:5000/api/problems/AIME/check?year=2024&contest=I&num=${index+1}&answer=${answers[index]}`);
        verdict[index] = (await response.json())["verdict"] ? 1 : 2;
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

    let answers: string[] = new Array(15).fill("");
    let verdict: Number[] = new Array(15).fill(0);
</script>

<Resizable.PaneGroup direction="horizontal" class="min-w-full justify-center">
    <div class="w-1/2">
        <Resizable.Pane>
            <div class="m-3 p-1 space-y-3">
                {#each content as item, index}
                    <Card.Root>
                        <Card.Header>
                            <Card.Title>n{index + 1}</Card.Title>
                            <Card.Description>AIME</Card.Description>
                        </Card.Header>
                        <Card.Content class="space-y-3">
                            {@html item}

                            <div class="align-middle flex">
                                <div class="inline-block my-auto">
                                    <InputOTP.Root disabled={verdict[index] === 1} maxlength={3} pattern={REGEXP_ONLY_DIGITS}
                                                   bind:value={answers[index]} onkeydown={(event) => {if (event.key === "Enter") getVerdict(index)}}>
                                        {#snippet children({cells})}
                                            <InputOTP.Group>
                                                {#each cells as cell}
                                                    <InputOTP.Slot {cell}/>
                                                {/each}
                                            </InputOTP.Group>
                                        {/snippet}
                                    </InputOTP.Root>
                                </div>
<!--                                <div class="inline-block my-auto mx-2">-->
<!--                                    <Button disabled={answers[index].length !== 3 || verdict[index] === 1} variant="secondary" class="inline" onclick={() => getVerdict(index)}>Submit</Button>-->
<!--                                </div>-->
                                <div class="inline-block my-auto mx-2">
                                    {@html getHTML(verdict[index])}
                                </div>
                            </div>
                        </Card.Content>
                    </Card.Root>
                {/each}
            </div>
        </Resizable.Pane>
    </div>
    <!--    <Resizable.Handle/>-->
    <!--    <Resizable.Pane>-->
    <!--        <div class="m-3 p-1 space-y-3">-->
    <!--            asdf-->
    <!--        </div>-->
    <!--    </Resizable.Pane>-->
</Resizable.PaneGroup>

