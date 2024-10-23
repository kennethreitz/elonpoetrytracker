# SpaceX Poetry Tracker 🚀📝

A playful parody website that "tracks" the journey of a poem intended for Elon Musk, styled after flight trackers but for poetry delivery status. Built with HTML, CSS, and minimal JavaScript.

## Overview

This project creates a sophisticated dark-mode dashboard that monitors the fictional journey of a space-themed poem through SpaceX's communication channels. It's a creative blend of space industry aesthetics and literary ambitions, featuring:

- Real-time "tracking" status
- Engagement metrics
- Timeline monitoring
- Activity feed
- Particle animation background
- Smooth hover effects and transitions

## Features

- 🌑 Dark mode optimized design
- 🎯 Live status tracking simulation
- 🎨 Space-themed aesthetic with floating particles
- ✨ Smooth CSS animations and transitions
- 📱 Responsive layout
- 🖥️ Clean, modern UI inspired by mission control dashboards

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/spacex-poetry-tracker.git
```

2. Open `index.html` in your browser:
```bash
cd spacex-poetry-tracker
open index.html  # Mac
# or
start index.html  # Windows
```

## Deployment

### Local Development
Simply open `index.html` in your browser.

### Deploy to fly.io
1. Install the flyctl CLI
2. Initialize your fly.io app:
```bash
fly launch
```
3. Deploy:
```bash
fly deploy
```

## Technical Details

### Built With
- HTML5
- CSS3 (with custom animations)
- Vanilla JavaScript
- Tufte CSS (for typography)

### Key Components
- Particle background system
- CSS Grid for metric cards
- Custom scrollbar styling
- Gradient animations
- Interactive hover states

## The Poem

The tracked poem "ACCELERATE" is a tribute to SpaceX's innovative rocket recovery system:

```
ACCELERATE:
Such are the days of new
When Humanity's view grew
Intelligence is not on the horizon
But here, by the grace of
Fantastical cheer
Brazen, we blaze through fear
Accelerate to the moon
AND BEYOND!
Mars really isn't so far
Dream, for sleep will cease
Until curiosity's demands
Tremble, at peace
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Customization

### Modifying the Status
Update the status information in the HTML:
```html
<section class="tracking-status">
    <h2><span class="status-indicator"></span>Current Status</h2>
    <p>Location: [New Location]</p>
    <p>Reading Status: [New Status]</p>
    <p>Time Since Submission: [New Time]</p>
</section>
```

### Changing Colors
The main color scheme can be modified in the CSS variables:
```css
:root {
    --primary-blue: #0088ff;
    --accent-red: #ff4136;
    --background-dark: #0a0a0a;
}
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

- Inspired by various flight tracking websites
- Typography inspired by Edward Tufte's design principles
- Particle animation inspired by space debris visualization

## Project Status

This is a parody project created for entertainment purposes. No actual tracking or monitoring of any individuals is performed. All metrics and statuses are fictional and for demonstration purposes only.

## Contact

Sarah Reitz - Poetry for Mars Initiative
Phone: (540)-398-6411

---

*Note: This is a creative project and is not affiliated with SpaceX, Tesla, or Elon Musk.*
