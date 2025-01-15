<script>

    import * as Sidebar from "$lib/components/ui/sidebar/index.ts";
    import AppSidebar from "$lib/components/app-sidebar.svelte";
    import {ModeWatcher, toggleMode} from "mode-watcher";
    import {Button} from "$lib/components/ui/button/index.ts";
    import {Moon, Sun} from "lucide-svelte";
    import * as Menubar from "$lib/components/ui/menubar/index.ts";
    import {Separator} from "$lib/components/ui/separator/index.ts";

    let {children} = $props();
</script>

<Sidebar.Provider>
    <AppSidebar/>
    <main class="w-screen h-screen">
        <div class="">
            <div class="m-3 fixed">
                <Sidebar.Trigger/>
            </div>
            <div class="float-right w-12">
                <div class="text-right m-1 fixed h-screen">
                    <Button onclick={toggleMode} variant="outline" size="icon">
                        <Sun
                                class="h-[1.2rem] w-[1.2rem] rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0"
                        />
                        <Moon
                                class="absolute h-[1.2rem] w-[1.2rem] rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100"
                        />
                        <span class="sr-only">Toggle theme</span>
                    </Button>
                </div>
            </div>
            {@render children?.()}
        </div>
        <ModeWatcher/>
    </main>
</Sidebar.Provider>
