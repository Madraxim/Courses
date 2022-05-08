class VideoProweb {
    static created = false
    constructor(data) {
        this.el = document.querySelector(data.el)
        this.elClass = data.el.replace('.', '')
        if (!VideoProweb.created) {
            this.create()
            VideoProweb.created = false
        }
        this.rate = this.el.getAttribute('data-rate').split(',').map(a => Number(a.trim()))
        this.video = document.querySelector(`.${this.elClass}__src`)
        this.div = document.querySelector(`.${this.elClass} > div`)
        this.btn = document.querySelector(`.${this.elClass}__btn`)
        this.currentTime = document.querySelector(`.${this.elClass}__time-current`)
        this.current = document.querySelector(`.${this.elClass}__time-currentVideo`)
        this.dur = document.querySelector(`.${this.elClass}__time-dVideo`)
        this.time = document.querySelector(`.${this.elClass}__time`)
        this.volume = document.querySelector(`.${this.elClass}__volume`)
        this.volumeC = document.querySelector(`.${this.elClass}__volume-current`)
        this.volumeBtn = document.querySelector(`.${this.elClass}__volume-btn i`)
        this.fulls = document.querySelector(`.${this.elClass}__fullscreen`)
        this.fulli = document.querySelector(`.${this.elClass}__fullscreen i`)


        this.lineFlag = false
        this.video.addEventListener('loadstart', this.timeRun)
        this.btn.addEventListener('click', () => this.play())
        this.div.addEventListener('dblclick', (e) => this.rewind(e))
        this.div.addEventListener('mouseenter', (e) => this.over(e))
        this.div.addEventListener('mouseleave', (e) => this.leave(e))
        this.div.addEventListener('contextmenu', (e) => this.contextmenu(e))
        this.video.addEventListener('timeupdate', () => this.timeupdate())
        this.video.addEventListener('volumechange', (e) => this.volumechange(e))
        this.time.addEventListener('mousedown', (e) => this.down(e))
        this.time.addEventListener('touchstart', (e) => this.down(e))
        window.addEventListener('mouseup', (e) => this.up(e))
        window.addEventListener('touchend', (e) => this.up(e))
        this.div.addEventListener('mousemove', (e) => this.move(e))
        this.div.addEventListener('touchmove', (e) => this.move(e))
        this.time.addEventListener('click', (e) => this.click(e))
        this.volume.addEventListener('wheel', (e) => this.wheel(e))
        this.fulls.addEventListener('click', (e) => this.full(e))

        // this.video
    }
    create() {
        const head = document.querySelector('head')

        head.innerHTML += `<style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        .${this.elClass} {
            width: 100%;
            position: relative;
            user-select: none;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .${this.elClass} > div {
            position: absolute;
            width: 100%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            top: 0;
            transition: 200ms;
            background: rgba(0,0,0,0.5)
        }
        .${this.elClass}__src {
            width: 100%;
            display: block;
        }
        .${this.elClass}__content {
            position: absolute;
            bottom: 0;
            background: linear-gradient(to top, rgba(0, 0, 0, 0.8), transparent);
            width: 100%;
            padding:40px 10px 20px;
        }
        .${this.elClass}__btn {
            position: absolute;
            border: none;
            outline: none;
            background: transparent;
            font-size: 50px;
            cursor: pointer;
            color: #39208a;
        }
        .${this.elClass}__time {
            width: 100%;
            background: rgba(255, 255, 255, 0.39);
            bottom: 15px;
            height: 10px;
            position: relative;
            display: flex;
        }
        .${this.elClass}__time::after {
            content: '';
            width: 14px;
            height: 14px;
            border-radius: 50%;
            background: #fff;
            display: block;
            margin-top: -2px;
            margin-left: -5px;
            cursor: pointer;
            transition: 200ms;
        }
        .${this.elClass}__content:hover .${this.elClass}__time::after {
            transform: scale(1.5);
        }
        .${this.elClass}__time-current {
            background:  #39208a;
            width: 0%;
            height: 100%;
        }
        .${this.elClass}__volume {
            display: flex;
            flex-direction: column-reverse;
            align-items: center;
            width: max-content;
        }
        .${this.elClass}__volume-btn {
            background: transparent;
            border: none;
            outline: none;
            color: #fff;
            cursor: pointer;
            font-size: 20px;
            width: 30px;
        }
        .${this.elClass}__volume-content {
            background: #fff;
            position: absolute;
            padding: 8px;
            border-radius: 4px;
            margin-bottom: 30px;
            opacity: 0;
            transform: scale(0.8) translateY(20px);
            transition: 200ms;
            visibility: hidden;
        }
        .${this.elClass}__volume-full {
            background: rgba(57, 32, 138, 0.3);
            height: 100px;
            width: 5px;
            display: flex;
            align-items: flex-end;
        }
        .${this.elClass}__volume-current {
            width: 100%;
            height: 100%;
            background: #39208a;
        }
        .${this.elClass}__volume:hover .${this.elClass}__volume-content {
            transform: scale(1) translateY(0);
            opacity: 1;
            visibility: visible;
        }
        .${this.elClass}__footer {
            display:flex;
            align-items: center;
            color: white
        }
        .${this.elClass}__time-dVideo {
            flex-grow: 1;
            text-align: right;
        }
        .${this.elClass}__time-currentVideo {
            margin-right: 20px;
        }
        .${this.elClass}__fullscreen {
            cursor: pointer;
            font-size: 20px;
            margin-left: 15px;
        }
        
        </style>`

        const src = this.el.getAttribute('data-src')
        this.el.removeAttribute('data-src')
        const video = `<video src="${src}" class="${this.elClass}__src"></video>`
        const btn = `<button class="${this.elClass}__btn"><i class="fas fa-play"></i></button>`
        const content = `
        <div class="${this.elClass}__content">
            <div class="${this.elClass}__time">
                <div class="${this.elClass}__time-current"></div>
            </div>
            <div class="${this.elClass}__footer">
                <span class="${this.elClass}__time-currentVideo">00:00</span>
                <div class="${this.elClass}__volume">
                    <button class="${this.elClass}__volume-btn">
                    <i class="fal fa-volume-up"></i>
                </button>
                <div class="${this.elClass}__volume-content">
                    <div class="${this.elClass}__volume-full">
                        <div class="${this.elClass}__volume-current">
                        </div>
                    </div>
                </div>
            </div>
                <span class="${this.elClass}__time-dVideo">00:00</span>
                <span class="${this.elClass}__fullscreen"><i class="fal fa-expand-wide"></i></span>
        </div>`
        this.el.innerHTML = `${video}<div>${btn}${content}</div>`
    }
    play() {
        if (this.video.paused) {
            this.video.play()
            this.btn.querySelector('.fas.fa-play').className = 'fas fa-pause'
        } else {
            this.video.pause()
            this.btn.querySelector('.fas.fa-pause').className = 'fas fa-play'
        }
    }
    timeupdate() {
        this.currentTime.style.width = 100 * this.video.currentTime / this.video.duration + '%'
        this.timeRun();
    }
    down() {
        this.lineFlag = true
        console.log(1);
    }
    up() {
        this.lineFlag = false
    }
    move(e) {
        if (this.lineFlag) {
            // console.log(e);
            const clickX = e.type === 'mousemove' ? e.offsetX : e.changedTouches[0].clientX - this.el.getBoundingClientRect().x
            console.log(clickX, this.el.clientWidth);
            const lineWidth = this.time.clientWidth 
            const persent = 100 * clickX / lineWidth
            this.currentTime.style.width = persent + '%'
            this.video.currentTime = this.video.duration * persent / 100
        }
    }
    click(e) {
        const clickX = e.offsetX
        const lineWidth = this.time.clientWidth
        const persent = 100 * clickX / lineWidth
        this.currentTime.style.width = persent + '%'
        this.video.currentTime = this.video.duration * persent / 100
    }
    wheel(e) {
        e.preventDefault();
        const delta = e.deltaY
        if (delta > 0) {
            if (this.video.volume > 0.1001) {
                this.video.volume -= 0.1
            } else {
                this.video.volume = 0
            }
        } else if (delta < 0) {
            if (this.video.volume > 0.999) {
                this.video.volume = 1
            } else {
                this.video.volume += 0.1
            }
        }

        const volPr = Math.floor(this.video.volume * 100)

        this.volumeC.style.height = volPr + '%'
    }
    rewind(e) {
        const videos = 100 * e.offsetX / this.video.clientWidth
        if (videos > 80) {
            this.video.currentTime += 15
        } else if(videos < 20) {
            this.video.currentTime -= 15
        } else {
            this.full()
        }

    }
    over(e) {
        this.div.style.opacity = 1;
    }
    leave(e) {
        // if (!this.video.paused) {
            this.div.style.opacity = 0;
        // }
    }
    timeDecoder(time) {
        let seconds = Math.floor(time % 60),
            hours   = Math.floor(time / 60 / 60),
            minutes = Math.floor(time / 60) - (hours * 60);
        minutes = minutes < 10 ? `0${minutes}` : minutes
        seconds = seconds < 10 ? `0${seconds}` : seconds

        const hms = hours > 0 ? `${hours}:${minutes}:${seconds}` : `${minutes}:${seconds}`

        return hms
    }
    timeRun() {
        this.current.innerHTML = this.timeDecoder(this.video.currentTime)
        this.dur.innerHTML = this.timeDecoder(this.video.duration)
    }
    volumechange(e) {
        if (this.video.volume >= 0.5) {
            this.volumeBtn.className = 'fal fa-volume-up'
            localStorage.volume = this.video.volume
        } else if (this.video.volume < 0.5 && this.video.volume > 0) {
            this.volumeBtn.className = 'fal fa-volume'
            localStorage.volume = this.video.volume
        } else {
            this.volumeBtn.className = 'fal fa-volume-slash'
        }
    }
    full(e) {
        if (this.el.requestFullScreen) {
            this.el.requestFullScreen();
        } else if (this.el.mozRequestFullScreen) {
            this.el.mozRequestFullScreen();
        } else if (this.el.webkitRequestFullScreen) {
            this.el.webkitRequestFullScreen();
        }
        if (document.cancelFullScreen) {
            document.cancelFullScreen();
        } else if (document.mozCancelFullScreen) {
            document.mozCancelFullScreen();
        } else if (document.webkitCancelFullScreen) {
            document.webkitCancelFullScreen();
        }

    }
    contextmenu(e) {
        e.preventDefault();
    }
}

const videoData = {
    el: '.video',
    colors: {

    }
}
const video= new VideoProweb(videoData)


