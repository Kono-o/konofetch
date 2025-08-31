import asyncio, time
from asyncio import sleep, create_task, run
from .state import State
from .fetch import fastfetch
from .layout import app
from prompt_toolkit.application import get_app

tick_queue = asyncio.Queue()

def update_fps():
    now = time.time()
    delta = now - State._last_time
    State._last_time = now
    instant_fps = 1 / delta if delta > 0 else 0
    alpha = 0.2
    State.fps = (1 - alpha) * State.fps + alpha * instant_fps
    State.fps = round(State.fps, 1)

def update():
    update_fps()

async def tick_listener():
    while True:
        await tick_queue.get()
        State.frame = (State.frame + 1) % 1000000
        update()

async def render_loop():
    while True:
        get_app().invalidate()
        await tick_queue.put("tick")
        frame_time = 1 / State.target_fps
        await sleep(frame_time)

async def fetch_info():
    loop = asyncio.get_running_loop()
    info = await loop.run_in_executor(None, fastfetch)
    if info:
        State.info = info
        State.is_up = True

async def main():
    create_task(render_loop())
    create_task(tick_listener())
    create_task(fetch_info())
    await app.run_async()


def entrypoint():
    asyncio.run(main())