<script>
    import "../app.css"

    import {ModeWatcher} from "mode-watcher";
    import {Separator} from "$lib/components/ui/separator/index.ts";
    import {Button} from "$lib/components/ui/button/index.ts";
    import {Box} from "lucide-svelte";

    let {children} = $props();
</script>

<ModeWatcher/>

<div class="flex py-2 items-center justify-center">
    <Box class="inline-block mx-1"></Box>
    <h1 class="font-bold inline-block mr-36">Math</h1>
    <Button variant="ghost">Product</Button>
    <Button variant="ghost">Demo</Button>
    <Button variant="ghost">Demo</Button>
    <Button variant="ghost">Demo</Button>
    <Button variant="ghost">Demo</Button>
    <Button variant="outline" class="ml-36">Login</Button>
</div>
<Separator/>
{@render children?.()}