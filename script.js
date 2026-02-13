/* === Reason Moon — Album Player === */

const ALBUM_TAGS = {
    'album_1': [
        { text: 'Ambient', cls: '' },
        { text: 'Experimental', cls: 'warm' },
        { text: 'Glitch', cls: 'cool' }
    ],
    'album_2': [
        { text: 'Lo-fi', cls: '' },
        { text: 'Office Vibes', cls: 'warm' },
        { text: 'Chill', cls: 'cool' }
    ],
    'album_3': [
        { text: 'K-Pop', cls: 'warm' },
        { text: 'Korean Market', cls: '' },
        { text: 'Fun', cls: 'cool' }
    ],
    'album_4': [
        { text: 'Curiosity', cls: 'warm' },
        { text: 'Experimental', cls: '' },
        { text: 'Multi-Genre', cls: 'cool' }
    ],
    'album_5': [
        { text: 'Art Pop', cls: 'warm' },
        { text: 'Concept Album', cls: '' },
        { text: 'Korean', cls: 'cool' }
    ]
};

let discography = [];
let currentAlbumIdx = -1;
let currentTrackIdx = -1;
let currentVersion = 0;
let isPlaying = false;

// Web Audio API
let audioCtx = null;
let analyserNode = null;
let sourceNode = null;
let visualizerInitialized = false;

const audio = document.getElementById('audio-player');
const albumsGrid = document.getElementById('albums-grid');
const albumDetail = document.getElementById('album-detail');
const playerBar = document.getElementById('player-bar');
const progressBar = document.getElementById('progress-bar');
const progressFill = document.getElementById('progress-fill');

// === Web Audio + Visualizer Setup ===
function initAudioContext() {
    if (audioCtx) return; // Already initialized
    try {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        analyserNode = audioCtx.createAnalyser();
        analyserNode.fftSize = 256;
        analyserNode.smoothingTimeConstant = 0.8;

        sourceNode = audioCtx.createMediaElementSource(audio);
        sourceNode.connect(analyserNode);
        analyserNode.connect(audioCtx.destination);
        console.log('[Visualizer] AudioContext initialized successfully');
    } catch (e) {
        console.error('[Visualizer] AudioContext init failed:', e);
        audioCtx = null;
        analyserNode = null;
    }
}

function initVisualizer() {
    if (visualizerInitialized) return;
    const canvas = document.getElementById('visualizer-canvas');
    if (!canvas || !analyserNode) {
        console.warn('[Visualizer] Cannot init - canvas:', !!canvas, 'analyser:', !!analyserNode);
        return;
    }
    // Force canvas pixel dimensions to match viewport
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    console.log('[Visualizer] Canvas dimensions:', canvas.width, 'x', canvas.height);
    
    Visualizer.init(canvas, analyserNode);
    visualizerInitialized = true;
    console.log('[Visualizer] Started successfully, type:', Visualizer.visualizationType);
}

// === Init ===
async function init() {
    try {
        const res = await fetch('assets/discography.json');
        discography = await res.json();
        renderAlbumCards();
        setupEventListeners();
    } catch (e) {
        console.error('Failed to load discography:', e);
        albumsGrid.innerHTML = '<p style="color:var(--text-muted);text-align:center;">Failed to load albums. Please check discography.json.</p>';
    }
}

// === Render Album Cards ===
function renderAlbumCards() {
    document.getElementById('album-count').textContent = discography.length;
    let totalTracks = 0;
    discography.forEach(a => totalTracks += a.tracks.length);
    document.getElementById('track-count').textContent = totalTracks;

    albumsGrid.innerHTML = discography.map((album, idx) => {
        const tags = ALBUM_TAGS[album.id] || [{ text: 'Music', cls: '' }];
        const tagHTML = tags.map(t => `<span class="tag ${t.cls}">${t.text}</span>`).join('');
        return `
        <div class="album-card" data-album-idx="${idx}">
            <div class="album-card-cover">
                <img src="${album.cover_art}" alt="${album.title}" loading="lazy">
                <div class="album-card-overlay">
                    <button class="album-card-play">▶</button>
                </div>
            </div>
            <div class="album-card-info">
                <h3 class="album-card-title">${album.title}</h3>
                <p class="album-card-meta">${album.artist} · ${album.tracks.length} tracks</p>
                <div class="album-card-tags">${tagHTML}</div>
            </div>
        </div>`;
    }).join('');
}

// === Show Album Detail ===
function showAlbumDetail(idx) {
    currentAlbumIdx = idx;
    const album = discography[idx];

    document.getElementById('album-cover-img').src = album.cover_art;
    document.getElementById('album-title-large').textContent = album.title;
    document.getElementById('album-artist').textContent = album.artist;
    document.getElementById('album-track-count').textContent = `${album.tracks.length} Tracks`;

    const trackList = document.getElementById('track-list');
    trackList.innerHTML = album.tracks.map((track, tIdx) => {
        const hasLyrics = track.lyrics && track.lyrics !== '[Instrumental / Lyrics Unavailable]';
        return `
        <div class="track-item" data-track-idx="${tIdx}">
            <span class="track-num">${String(tIdx + 1).padStart(2, '0')}</span>
            <img class="track-thumb" src="${track.art}" alt="${track.title}" loading="lazy">
            <div class="track-title-col">
                <span class="track-title">${track.title}</span>
            </div>
            ${hasLyrics ? `<button class="track-lyrics-btn" data-track-idx="${tIdx}">Lyrics</button>` : '<span></span>'}
            <span class="track-duration">—</span>
        </div>`;
    }).join('');

    albumDetail.style.display = 'block';
    document.getElementById('albums').scrollIntoView({ behavior: 'smooth', block: 'start' });

    // Update nav
    document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
    document.querySelector('.nav-link[href="#now-playing"]').classList.add('active');
}

function hideAlbumDetail() {
    albumDetail.style.display = 'none';
    currentAlbumIdx = -1;
    document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));
    document.querySelector('.nav-link[href="#albums"]').classList.add('active');
}

// === Play Track ===
function playTrack(albumIdx, trackIdx, version = 0) {
    currentAlbumIdx = albumIdx;
    currentTrackIdx = trackIdx;
    currentVersion = version;

    const album = discography[albumIdx];
    const track = album.tracks[trackIdx];
    const ver = track.versions[version] || track.versions[0];

    // Set source first
    audio.src = ver.file;

    // Init Web Audio API on first user interaction (must be after src is set)
    initAudioContext();
    if (audioCtx && audioCtx.state === 'suspended') {
        audioCtx.resume();
    }

    // Init visualizer immediately (don't wait for play promise)
    initVisualizer();

    audio.play().then(() => {
        const vizCanvas = document.getElementById('visualizer-canvas');
        if (vizCanvas) vizCanvas.classList.add('active');
    }).catch(e => console.warn('Autoplay blocked:', e));
    isPlaying = true;

    // Update player bar
    playerBar.style.display = 'block';
    document.getElementById('player-thumb').src = track.art;
    document.getElementById('player-track-title').textContent = track.title;
    document.getElementById('player-album-name').textContent = album.title;
    document.getElementById('btn-play').textContent = '⏸';

    // Update version select
    const vSelect = document.getElementById('version-select');
    vSelect.innerHTML = track.versions.map((v, i) =>
        `<option value="${i}" ${i === version ? 'selected' : ''}>${v.name}</option>`
    ).join('');

    // Highlight active track
    document.querySelectorAll('.track-item').forEach(el => el.classList.remove('active'));
    const activeItem = document.querySelector(`.track-item[data-track-idx="${trackIdx}"]`);
    if (activeItem) activeItem.classList.add('active');
}

// === Player Controls ===
function togglePlay() {
    if (!audio.src) return;
    const vizCanvas = document.getElementById('visualizer-canvas');
    if (isPlaying) {
        audio.pause();
        document.getElementById('btn-play').textContent = '▶';
        if (vizCanvas) vizCanvas.classList.remove('active');
    } else {
        audio.play();
        document.getElementById('btn-play').textContent = '⏸';
        if (vizCanvas) vizCanvas.classList.add('active');
    }
    isPlaying = !isPlaying;
}

function nextTrack() {
    if (currentAlbumIdx < 0) return;
    const album = discography[currentAlbumIdx];
    let next = currentTrackIdx + 1;
    if (next >= album.tracks.length) {
        // Go to next album
        let nextAlbum = (currentAlbumIdx + 1) % discography.length;
        playTrack(nextAlbum, 0, 0);
        showAlbumDetail(nextAlbum);
    } else {
        playTrack(currentAlbumIdx, next, 0);
    }
}

function prevTrack() {
    if (currentAlbumIdx < 0) return;
    if (audio.currentTime > 3) {
        audio.currentTime = 0;
        return;
    }
    let prev = currentTrackIdx - 1;
    if (prev < 0) {
        let prevAlbum = (currentAlbumIdx - 1 + discography.length) % discography.length;
        playTrack(prevAlbum, discography[prevAlbum].tracks.length - 1, 0);
        showAlbumDetail(prevAlbum);
    } else {
        playTrack(currentAlbumIdx, prev, 0);
    }
}

function formatTime(s) {
    if (isNaN(s)) return '0:00';
    const m = Math.floor(s / 60);
    const sec = Math.floor(s % 60);
    return `${m}:${String(sec).padStart(2, '0')}`;
}

// === Lyrics ===
function showLyrics(albumIdx, trackIdx) {
    const track = discography[albumIdx].tracks[trackIdx];
    document.getElementById('lyrics-song-title').textContent = track.title;
    document.getElementById('lyrics-text').textContent = track.lyrics || 'No lyrics available.';
    document.getElementById('lyrics-modal').style.display = 'flex';
}

function hideLyrics() {
    document.getElementById('lyrics-modal').style.display = 'none';
}

// === Event Listeners ===
function setupEventListeners() {
    // Album cards
    albumsGrid.addEventListener('click', (e) => {
        const card = e.target.closest('.album-card');
        if (!card) return;
        const idx = parseInt(card.dataset.albumIdx);
        const playBtn = e.target.closest('.album-card-play');
        if (playBtn) {
            showAlbumDetail(idx);
            playTrack(idx, 0, 0);
        } else {
            showAlbumDetail(idx);
        }
    });

    // Back button
    document.getElementById('back-btn').addEventListener('click', hideAlbumDetail);

    // Track list
    document.getElementById('track-list').addEventListener('click', (e) => {
        const lyricsBtn = e.target.closest('.track-lyrics-btn');
        if (lyricsBtn) {
            e.stopPropagation();
            showLyrics(currentAlbumIdx, parseInt(lyricsBtn.dataset.trackIdx));
            return;
        }
        const item = e.target.closest('.track-item');
        if (item) {
            playTrack(currentAlbumIdx, parseInt(item.dataset.trackIdx), 0);
        }
    });

    // Player controls
    document.getElementById('btn-play').addEventListener('click', togglePlay);
    document.getElementById('btn-next').addEventListener('click', nextTrack);
    document.getElementById('btn-prev').addEventListener('click', prevTrack);

    // Version select
    document.getElementById('version-select').addEventListener('change', (e) => {
        playTrack(currentAlbumIdx, currentTrackIdx, parseInt(e.target.value));
    });

    // Volume
    document.getElementById('volume-slider').addEventListener('input', (e) => {
        audio.volume = e.target.value / 100;
    });
    audio.volume = 0.8;

    // Progress
    audio.addEventListener('timeupdate', () => {
        if (audio.duration) {
            const pct = (audio.currentTime / audio.duration) * 100;
            progressFill.style.width = pct + '%';
            document.getElementById('time-current').textContent = formatTime(audio.currentTime);
            document.getElementById('time-total').textContent = formatTime(audio.duration);
        }
    });

    progressBar.addEventListener('click', (e) => {
        const rect = progressBar.getBoundingClientRect();
        const pct = (e.clientX - rect.left) / rect.width;
        audio.currentTime = pct * audio.duration;
    });

    // Auto next
    audio.addEventListener('ended', nextTrack);

    // Lyrics modal
    document.getElementById('lyrics-close').addEventListener('click', hideLyrics);
    document.getElementById('lyrics-modal').addEventListener('click', (e) => {
        if (e.target === e.currentTarget) hideLyrics();
    });

    // Keyboard
    document.addEventListener('keydown', (e) => {
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'SELECT') return;
        switch (e.code) {
            case 'Space': e.preventDefault(); togglePlay(); break;
            case 'ArrowRight': nextTrack(); break;
            case 'ArrowLeft': prevTrack(); break;
        }
    });

    // Visualizer mode controls
    const vizControls = document.getElementById('visualizer-controls');
    if (vizControls) {
        vizControls.addEventListener('click', (e) => {
            const btn = e.target.closest('.viz-btn');
            if (!btn) return;
            const mode = btn.dataset.viz;
            vizControls.querySelectorAll('.viz-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            if (window.Visualizer) Visualizer.setType(mode);
        });
    }

    // Nav links
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', (e) => {
            if (link.getAttribute('href') === '#albums') {
                hideAlbumDetail();
            }
        });
    });
}

// === Start ===
document.addEventListener('DOMContentLoaded', init);
