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
        this.canvas.width = this.canvas.clientWidth;
        this.canvas.height = this.canvas.clientHeight;
    },

    initParticles: function() {
        this.particles = [];
        const particleCount = 100;
        for (let i = 0; i < particleCount; i++) {
            this.particles.push({
                x: Math.random() * this.canvas.width,
                y: Math.random() * this.canvas.height,
                radius: Math.random() * 3 + 1,
                color: `rgba(255, 255, 255, ${Math.random() * 0.5 + 0.5})`,
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

        // Clear
        this.ctx.clearRect(0, 0, width, height);

        // Transparent background
        // this.ctx.fillStyle = 'rgba(0, 0, 0, 0)'; 

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
        this.ctx.beginPath();
        
        // Calculate Wave Points
        let x = 0;
        const sliceWidth = width / bufferLength * 4; // Spread out more
        
        // Start from middle left
        this.ctx.moveTo(0, height / 2);

        // Spline through points
        for (let i = 0; i < bufferLength; i++) {
           if (x > width) break;
           
           const v = dataArray[i] / 255;
           const y = v * (height * 0.4); // Amplitude scaling
           
           // We want the wave to be centered vertically, reacting up and down
           // But frequency data is 0-255. 0 is silence.
           // Let's make it a floor wave at the bottom 1/3
           
           // Simple wave approach from reference
           const waveY = (height * 0.7) - y;
           
           // Quadratic curve for smoothness
            // Wait, we need pairs for quadratic. keep it simple for now or use the ref logic.
            // Reference logic: 
            /*
            const midX = x + sliceWidth / 2;
            const midY = (y + (dataArray[i + 1] / 255) * height) / 2;
            ctx.quadraticCurveTo(x, y, midX, midY);
            */
            // Let's just draw lines for robustness first in vanilla
            this.ctx.lineTo(x, waveY);
            
            x += sliceWidth;
        }

        this.ctx.lineTo(width, height);
        this.ctx.lineTo(0, height);
        this.ctx.fillStyle = 'rgba(29, 185, 84, 0.2)'; // Primary color tint
        this.ctx.fill();
        
        // Stroke
        this.ctx.strokeStyle = 'rgba(29, 185, 84, 0.8)';
        this.ctx.lineWidth = 2;
        this.ctx.stroke();
    },

    drawOceanParticles: function(dataArray, width, height) {
        const numParticles = this.particles.length;
        const movementScale = 2;
        const dataNormalizationFactor = 1 / 255;

        for (let i = 0; i < numParticles; i++) {
            const particle = this.particles[i];
            this.ctx.beginPath();
            this.ctx.arc(particle.x, particle.y, particle.radius, 0, Math.PI * 2);
            this.ctx.fillStyle = particle.color;
            this.ctx.fill();

            // Movement reacting to bass (low freqs)
            const dataIndex = i % 20; // Use low frequencies
            const dataValue = dataArray[dataIndex];
            const normalizedMovement = (dataValue * dataNormalizationFactor); 
            
            particle.y -= normalizedMovement * 1; // Float up with bass
            particle.x += Math.sin(particle.y * 0.05);

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

            const hue = i * 2; // Rainbow
            this.ctx.fillStyle = `hsla(${hue}, 80%, 50%, 0.8)`;
            
            this.ctx.fillRect(x, height - barHeight, barWidth, barHeight);

            x += barWidth + 1;
            if (x > width) break;
        }
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
