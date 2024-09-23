function shoScore (scr: number) {
    light.setAll(0x000000)
    for (let index = 0; index <= scr - 1; index++) {
        light.setPixelColor(index, 0x00ff00)
    }
}
function resume () {
    Active = true
}
function pause2 () {
    light.setAll(0x000000)
    Active = false
}
function Init () {
    ships = 10
    score = 0
    Active = true
    light.showAnimation(light.sparkleAnimation, 500)
    light.setAll(0x000000)
    launch = false
    dlta = 1
    ldelta = 1
    sloc = 0
    wloc = wormhole[sloc]
    ship = Colors.Green
    station = Colors.Blue
    whole = Colors.Indigo
    wormhole = [5, 6, 7, 8, 9, 0, 1, 2, 3, 4]
    if (input.switchRight()) {
        music.setVolume(100)
    } else {
        music.setVolume(0)
    }
}
function display (statloc: number, delta: number) {
    light.setPixelColor(statloc, 0x000000)
    light.setPixelColor(wormhole[statloc], 0x000000)
    sloc = sloc + delta
    if (sloc < 0) {
        sloc = 9
    }
    if (sloc > 9) {
        sloc = 0
    }
    wloc = wormhole[sloc]
    light.setPixelColor(sloc, station)
    light.setPixelColor(wloc, whole)
}
input.onGesture(Gesture.Shake, function () {
    pause2()
    light.showAnimation(light.theaterChaseAnimation, 500)
    Init()
})
input.buttonB.onEvent(ButtonEvent.Click, function () {
    if (ships > 0 && Active) {
        music.pewPew.play()
        launch = true
        ldelta = -1
        ships += -1
    }
})
input.onSwitchMoved(SwitchDirection.Left, function () {
    music.setVolume(0)
})
input.onSwitchMoved(SwitchDirection.Right, function () {
    music.setVolume(100)
})
input.buttonA.onEvent(ButtonEvent.Click, function () {
    if (ships > 0 && Active) {
        music.pewPew.play()
        launch = true
        ldelta = 1
        ships += -1
    }
})
let shiploc = 0
let whole = 0
let station = 0
let ship = 0
let wormhole: number[] = []
let wloc = 0
let sloc = 0
let ldelta = 0
let dlta = 0
let launch = false
let score = 0
let ships = 0
let Active = false
Init()
resume()
forever(function () {
    if (Active) {
        whole = light.rgb(Math.randomRange(13, 200), Math.randomRange(13, 200), Math.randomRange(13, 200))
        pause(200)
    }
})
forever(function () {
    if (5 < Math.randomRange(0, 10)) {
        dlta = -1
    } else {
        dlta = 1
    }
    pause(100 * Math.randomRange(1, 10))
})
forever(function () {
    if (launch) {
        launch = false
        ship = Colors.Green
        shiploc = sloc
        for (let i = 0; i < 5; i++) {
            light.setPixelColor(shiploc, ship)
            pause(100)
            light.setPixelColor(shiploc, 0x000000)
            if (wloc == shiploc) {
                light.showAnimation(light.rainbowAnimation, 500)
                music.magicWand.play()
                ldelta = 0
                ship = Colors.Black
                score += 1
            } else {
                shiploc = shiploc + ldelta
                if (shiploc < 0) {
                    shiploc = 9
                }
                if (shiploc > 9) {
                    shiploc = 0
                }
                light.setPixelColor(shiploc, ship)
            }
        }
        light.setAll(0x000000)
    }
})
forever(function () {
    if (Active) {
        display(sloc, dlta)
        pause(350)
    }
})
forever(function () {
    if (ships < 1) {
        pause2()
        shoScore(score)
    }
    pause(1000)
})
