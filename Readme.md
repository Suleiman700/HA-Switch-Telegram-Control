
# HA Switches Telegram Control

### Description

With this repo, You can control your HA switches using via Telegram voice message.

### Flow

![flow.png](..%2Fimgs%2Fflow.png)

### Installation

#### A. Install the `python-server` in Docker
1. Change the `port` in python server script `main.py` & `Dockerfile`.

2. Build & Run server, Commands can be found at the bottom of `Dockerfile` file.

---

#### B. Add new `Node-Red` flow and import `Node-Red flow.txt`.

---

#### C. Create Telegram bot and configure it in Node-Red.

---

#### D. Configure Node-Red script

trigger_words: This is the phrase you should say
entities: The entities that will be targeted when saying that trigger words

```javascript
// Define a dictionary of trigger words and their corresponding entities
const entitiesDict = [
    // Living room
    {
        trigger_words: ['living room', 'living room light'], // Phrase to say
        entities: ['switch.living_room_light_1', 'switch.living_room_light_2'], // Targeted entities
    },
    {
        trigger_words: ['first floor'], // Phrase to say
        entities: ['switch.living_room_light_1', 'switch.kitchen', 'switch.x'], // Targeted entities
    },
];
```

![node-red.png](..%2Fimgs%2Fnode-red.png)

---

#### E. Send voice message to Telegram bot

![telegram-bot.png](..%2Fimgs%2Ftelegram-bot.png)