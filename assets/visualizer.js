// Visualizer Logic - Ported from React to Vanilla JS
// Source: audio-visualizer project

const Visualizer = {
    canvas: null,
    ctx: null,
    analyser: null,
    animationId: null,
    visualizationType: 'ocean', // Default
    particles: [],

    init: function(canvasElement, analyserNode) {
        this.canvas = canvasElement;
        this.ctx = canvasElement.getContext('2d');
        this.analyser = analyserNode;
        
        // Handle Resize
        this.resize();
        window.addEventListener('resize', () => this.resize());
        
        // Init Particles for Ocean
        this.initParticles();
        
        // Start loop
        this.animate();
    },

    resize: function() {
        if (!this.canvas) return;
        // Use window dimensions for fullscreen canvas, fallback to clientWidth
        this.canvas.width = this.canvas.clientWidth || window.innerWidth;
        this.canvas.height = this.canvas.clientHeight || window.innerHeight;
    },

    initParticles: function() {
        this.particles = [];
        const particleCount = 200;
        const colors = [
            [124, 92, 255],   // accent purple
            [0, 212, 170],    // accent teal
            [255, 107, 157],  // accent pink
            [200, 180, 255],  // light purple
        ];
        for (let i = 0; i < particleCount; i++) {
            const c = colors[Math.floor(Math.random() * colors.length)];
            this.particles.push({
                x: Math.random() * this.canvas.width,
                y: Math.random() * this.canvas.height,
                radius: Math.random() * 4 + 2,
                color: `rgba(${c[0]}, ${c[1]}, ${c[2]}, ${Math.random() * 0.4 + 0.4})`,
            });
        }
    },

    setType: function(type) {
        this.visualizationType = type;
        // Re-init if needed
        if (type === 'ocean') this.initParticles();
    },

    animate: function() {
        if (!this.canvas || !this.analyser) return;

        this.animationId = requestAnimationFrame(() => this.animate());

        const width = this.canvas.width;
        const height = this.canvas.height;
        const bufferLength = this.analyser.frequencyBinCount;
        const dataArray = new Uint8Array(bufferLength);
        
        // Get Data
        this.analyser.getByteFrequencyData(dataArray);

        // Clear canvas to transparent — waves appear as bright overlay on page
        this.ctx.clearRect(0, 0, width, height);

        switch (this.visualizationType) {
            case 'ocean':
                this.renderOcean(dataArray, width, height);
                break;
            case 'bars':
                this.renderBars(dataArray, width, height);
                break;
            case 'circle':
                this.renderCircle(dataArray, width, height);
                break;
            case 'waveform':
                this.renderWaveform(width, height);
                break;
            default:
                this.renderOcean(dataArray, width, height);
        }
    },

    renderOcean: function(dataArray, width, height) {
        // Draw Particles first
        this.drawOceanParticles(dataArray, width, height);
        
        // Draw Wave
        const bufferLength = dataArray.length;
        const sliceWidth = width / bufferLength * 4;
        
        // --- Wave path ---
        this.ctx.beginPath();
        this.ctx.moveTo(0, height * 0.7);
        let x = 0;

        for (let i = 0; i < bufferLength; i++) {
           if (x > width) break;
           const v = dataArray[i] / 255;
           const y = v * (height * 0.5);
           const waveY = (height * 0.7) - y;
           this.ctx.lineTo(x, waveY);
           x += sliceWidth;
        }

        this.ctx.lineTo(width, height);
        this.ctx.lineTo(0, height);
        this.ctx.closePath();

        // Bright gradient fill — cyan to purple, high opacity
        const grad = this.ctx.createLinearGradient(0, height * 0.2, 0, height);
        grad.addColorStop(0, 'rgba(0, 255, 200, 0.5)');
        grad.addColorStop(0.4, 'rgba(100, 140, 255, 0.35)');
        grad.addColorStop(1, 'rgba(124, 92, 255, 0.1)');
        this.ctx.fillStyle = grad;
        this.ctx.fill();
        
        // Neon GLOW stroke — white core
        this.ctx.shadowColor = 'rgba(0, 255, 200, 1)';
        this.ctx.shadowBlur = 25;
        this.ctx.strokeStyle = 'rgba(255, 255, 255, 1)';
        this.ctx.lineWidth = 2;
        this.ctx.stroke();
        
        // Outer glow
        this.ctx.shadowColor = 'rgba(124, 92, 255, 0.8)';
        this.ctx.shadowBlur = 40;
        this.ctx.strokeStyle = 'rgba(0, 255, 200, 0.8)';
        this.ctx.lineWidth = 3;
        this.ctx.stroke();
        this.ctx.shadowBlur = 0;
    },

    drawOceanParticles: function(dataArray, width, height) {
        const numParticles = this.particles.length;
        const dataNormalizationFactor = 1 / 255;

        for (let i = 0; i < numParticles; i++) {
            const particle = this.particles[i];
            
            // Glow effect for particles
            this.ctx.shadowColor = particle.color;
            this.ctx.shadowBlur = 8;
            this.ctx.beginPath();
            this.ctx.arc(particle.x, particle.y, particle.radius, 0, Math.PI * 2);
            this.ctx.fillStyle = particle.color;
            this.ctx.fill();
            this.ctx.shadowBlur = 0;

            // Movement reacting to bass (low freqs)
            const dataIndex = i % 30;
            const dataValue = dataArray[dataIndex];
            const normalizedMovement = (dataValue * dataNormalizationFactor); 
            
            particle.y -= normalizedMovement * 1.5;
            particle.x += Math.sin(particle.y * 0.03) * 1.2;

            // Reset
            if (particle.y < 0) particle.y = height;
            if (particle.x > width) particle.x = 0;
            if (particle.x < 0) particle.x = width;
        }
    },

    renderBars: function(dataArray, width, height) {
        const barWidth = (width / dataArray.length) * 2.5;
        let x = 0;

        for (let i = 0; i < dataArray.length; i++) {
            const v = dataArray[i];
            const percent = v / 255;
            const barHeight = percent * height * 0.8;

            const hue = 260 + (i * 0.8);
            this.ctx.shadowColor = `hsla(${hue}, 100%, 60%, 0.6)`;
            this.ctx.shadowBlur = 10;
            this.ctx.fillStyle = `hsla(${hue}, 90%, 60%, 0.9)`;
            
            this.ctx.fillRect(x, height - barHeight, barWidth, barHeight);

            x += barWidth + 1;
            if (x > width) break;
        }
        this.ctx.shadowBlur = 0;
    },

    renderCircle: function(dataArray, width, height) {
        const centerX = width / 2;
        const centerY = height / 2;
        const radius = Math.min(width, height) / 4;
        const bars = 100; // Limit bars for circle
        const radBuffer = dataArray.slice(0, bars); 

        for (let i = 0; i < bars; i++) {
            const angle = (i / bars) * Math.PI * 2;
            const v = radBuffer[i];
            const length = (v / 255) * radius;

            const x = centerX + Math.cos(angle) * (radius + length);
            const y = centerY + Math.sin(angle) * (radius + length);

            this.ctx.beginPath();
            this.ctx.moveTo(centerX + Math.cos(angle) * radius, centerY + Math.sin(angle) * radius);
            this.ctx.lineTo(x, y);
            this.ctx.strokeStyle = `hsl(${(i / bars) * 360}, 100%, 50%)`;
            this.ctx.lineWidth = 3;
            this.ctx.stroke();
        }
    },
    
    renderWaveform: function(width, height) {
         // Time Domain Data needs a different fetch method (getByteTimeDomainData)
         // For now, let's keep it simple and assume we switch buffer or skip
         // We will just draw a flat line or simple wave if freq data is used.
         // To do this properly, we need to switch the data source in the animate loop.
         // Skipping for MVP to keep file simple.
    }
};

window.Visualizer = Visualizer;
