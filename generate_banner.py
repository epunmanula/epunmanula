import os
import base64

dir_path = os.path.dirname(os.path.abspath(__file__))
b64_logo_path = os.path.join(dir_path, "emlogo.b64")
png_logo_path = os.path.join(dir_path, "emlogo.png")

if os.path.exists(b64_logo_path):
    with open(b64_logo_path, "r", encoding="utf-8") as f:
        logo_b64 = f.read().strip()
elif os.path.exists(png_logo_path):
    with open(png_logo_path, "rb") as f:
        logo_b64 = base64.b64encode(f.read()).decode("ascii")
else:
    logo_b64 = ""

out_path_1 = os.path.join(dir_path, "epun-manula-3d-banner.svg")
out_path_2 = r"c:\em\web\reeme\epun-manula-3d-banner.svg"

svg_template = f'''<svg width="1200" height="340" viewBox="0 0 1200 340" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <defs>
    <!-- Dark Cyber Canvas Gradient -->
    <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#060A12" />
      <stop offset="50%" stop-color="#04070D" />
      <stop offset="100%" stop-color="#020306" />
    </linearGradient>

    <!-- Emerald Neon Gradients -->
    <linearGradient id="emerald-glow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#1DB954" />
      <stop offset="50%" stop-color="#10B981" />
      <stop offset="100%" stop-color="#059669" />
    </linearGradient>

    <!-- Matrix Code Grid Pattern -->
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="rgba(29, 185, 84, 0.06)" stroke-width="1" />
      <circle cx="40" cy="40" r="1" fill="rgba(16, 185, 129, 0.25)" />
    </pattern>

    <!-- Filters for Glow & Shadows -->
    <filter id="blur-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="60" />
    </filter>
    
    <filter id="logo-glow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="15" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>

    <style>
      @keyframes spin3D {{
        0% {{ transform: perspective(600px) rotateY(0deg); }}
        50% {{ transform: perspective(600px) rotateY(180deg); }}
        100% {{ transform: perspective(600px) rotateY(360deg); }}
      }}
      @keyframes nameGlow {{
        0%, 100% {{
          fill: #FFFFFF;
          filter: drop-shadow(0px 0px 4px rgba(29, 185, 84, 0.3));
        }}
        50% {{
          fill: #E2F9EE;
          filter: drop-shadow(0px 0px 18px rgba(29, 185, 84, 0.95)) drop-shadow(0px 0px 28px rgba(16, 185, 129, 0.7));
        }}
      }}
      @keyframes badgePulse {{
        0%, 100% {{
          stroke-opacity: 0.4;
          fill-opacity: 0.12;
        }}
        50% {{
          stroke-opacity: 0.8;
          fill-opacity: 0.25;
        }}
      }}
      
      .logo-orbit {{
        transform-origin: 600px 55px;
        animation: spin3D 8s ease-in-out infinite;
      }}
      .logo-image-group {{
        transform-origin: 600px 55px;
        animation: spin3D 6s ease-in-out infinite;
      }}
      .animated-title {{
        animation: nameGlow 3.5s ease-in-out infinite;
      }}
      .cyber-badge {{
        animation: badgePulse 3s ease-in-out infinite;
      }}
    </style>
  </defs>

  <!-- Background Base Canvas -->
  <rect width="1200" height="340" rx="16" fill="url(#bg-grad)" />
  <rect width="1200" height="340" rx="16" fill="url(#grid)" />

  <!-- Ambient Glowing Orbs -->
  <circle cx="180" cy="170" r="180" fill="#1DB954" opacity="0.18" filter="url(#blur-glow)" />
  <circle cx="1020" cy="170" r="180" fill="#10B981" opacity="0.14" filter="url(#blur-glow)" />
  <circle cx="600" cy="65" r="120" fill="#1DB954" opacity="0.15" filter="url(#blur-glow)" />

  <!-- Outer Cyber Neon Border -->
  <rect x="1" y="1" width="1198" height="338" rx="15" fill="none" stroke="url(#emerald-glow)" stroke-opacity="0.4" stroke-width="2" />

  <!-- Left Side Tech Circuit Accents -->
  <g stroke="#1DB954" stroke-width="1.2" opacity="0.3" fill="none">
    <path d="M 30 50 L 150 50 L 180 80" />
    <path d="M 30 290 L 150 290 L 180 260" />
    <circle cx="30" cy="50" r="3" fill="#1DB954" />
    <circle cx="30" cy="290" r="3" fill="#1DB954" />
    <circle cx="180" cy="80" r="3" fill="#1DB954" />
    <circle cx="180" cy="260" r="3" fill="#1DB954" />
  </g>

  <!-- Right Side Tech Circuit Accents -->
  <g stroke="#10B981" stroke-width="1.2" opacity="0.3" fill="none">
    <path d="M 1170 50 L 1050 50 L 1020 80" />
    <path d="M 1170 290 L 1050 290 L 1020 260" />
    <circle cx="1170" cy="50" r="3" fill="#10B981" />
    <circle cx="1170" cy="290" r="3" fill="#10B981" />
    <circle cx="1020" cy="80" r="3" fill="#10B981" />
    <circle cx="1020" cy="260" r="3" fill="#10B981" />
  </g>

  <!-- LEFT SIDE TECH STACK ICONS (Compact Grid - No Text Names) -->
  <!-- 1. REACT LOGO -->
  <g transform="translate(60, 55)">
    <circle cx="20" cy="20" r="20" fill="rgba(10, 15, 25, 0.85)" stroke="#61DAFB" stroke-width="1.5" />
    <g transform="translate(20, 20) scale(0.6)">
      <ellipse rx="18" ry="7" fill="none" stroke="#61DAFB" stroke-width="2" />
      <ellipse rx="18" ry="7" fill="none" stroke="#61DAFB" stroke-width="2" transform="rotate(60)" />
      <ellipse rx="18" ry="7" fill="none" stroke="#61DAFB" stroke-width="2" transform="rotate(120)" />
      <circle r="3.5" fill="#61DAFB" />
    </g>
  </g>

  <!-- 2. NEXT.JS LOGO -->
  <g transform="translate(120, 55)">
    <circle cx="20" cy="20" r="20" fill="rgba(10, 15, 25, 0.85)" stroke="#FFFFFF" stroke-width="1.5" />
    <g transform="translate(10, 10) scale(0.7)">
      <circle cx="15" cy="15" r="14" fill="#000000" stroke="#FFFFFF" stroke-width="1" />
      <path d="M 21 21 L 11 8 L 9 8 L 9 22 L 12 22 L 12 12 L 19.5 22 Z" fill="#FFFFFF" />
      <rect x="18" y="8" width="3" height="7" fill="#FFFFFF" />
    </g>
  </g>

  <!-- 3. TYPESCRIPT LOGO -->
  <g transform="translate(60, 140)">
    <rect x="0" y="0" width="40" height="40" rx="10" fill="#3178C6" stroke="#FFFFFF" stroke-width="1.2" />
    <text x="20" y="27" text-anchor="middle" font-family="'Inter', sans-serif" font-weight="900" font-size="18" fill="#FFFFFF">TS</text>
  </g>

  <!-- 4. PHP LOGO -->
  <g transform="translate(120, 140)">
    <ellipse cx="20" cy="20" rx="22" ry="14" fill="#777BB4" stroke="#FFFFFF" stroke-width="1.2" />
    <text x="20" y="25" text-anchor="middle" font-family="'Fira Code', monospace" font-weight="900" font-size="13" fill="#FFFFFF">php</text>
  </g>

  <!-- 5. NODE.JS LOGO -->
  <g transform="translate(60, 225)">
    <circle cx="20" cy="20" r="20" fill="rgba(10, 15, 25, 0.85)" stroke="#22C55E" stroke-width="1.5" />
    <path d="M 20 9 L 30 15 L 30 26 L 20 31 L 10 26 L 10 15 Z" fill="none" stroke="#22C55E" stroke-width="1.8" />
    <path d="M 20 15 L 25 18 L 25 22 M 20 15 L 15 18 L 15 22" stroke="#86EFAC" stroke-width="1.8" stroke-linecap="round" />
  </g>

  <!-- 6. PYTHON LOGO -->
  <g transform="translate(120, 225)">
    <circle cx="20" cy="20" r="20" fill="rgba(10, 15, 25, 0.85)" stroke="#3776AB" stroke-width="1.5" />
    <g transform="translate(9, 9) scale(0.58)">
      <path d="M 19 2 C 11 2 11 6 11 6 L 11 10 L 19 10 L 19 12 L 7 12 C 2 12 2 19 2 19 L 2 25 C 2 30 7 30 7 30 L 11 30 L 11 25 C 11 20 16 20 16 20 L 24 20 C 29 20 29 15 29 15 L 29 9 C 29 3 24 2 19 2 Z" fill="#3776AB" />
      <path d="M 21 38 C 29 38 29 34 29 34 L 29 30 L 21 30 L 21 28 L 33 28 C 38 28 38 21 38 21 L 38 15 C 38 10 33 10 33 10 L 29 10 L 29 15 C 29 20 24 20 24 20 L 16 20 C 11 20 11 25 11 25 L 11 31 C 11 37 16 38 21 38 Z" fill="#FFD43B" />
    </g>
  </g>

  <!-- CENTER MAIN CONTENT -->
  <!-- 1. EMBEDDED ANIMATED ROTATING LOGO -->
  <g transform="translate(0, 0)">
    <!-- Glowing Backdrop Circle -->
    <circle cx="600" cy="55" r="36" fill="rgba(29, 185, 84, 0.22)" filter="url(#blur-glow)" />
    <circle cx="600" cy="55" r="34" fill="#04070D" stroke="url(#emerald-glow)" stroke-width="1.8" />
    
    <!-- Rotating Orbit Ring with Tech Nodes -->
    <g class="logo-orbit">
      <circle cx="600" cy="55" r="42" fill="none" stroke="#1DB954" stroke-width="1.5" stroke-dasharray="10 8 4 8" opacity="0.8" />
      <circle cx="600" cy="13" r="3.5" fill="#1DB954" />
      <circle cx="642" cy="55" r="2.5" fill="#10B981" />
      <circle cx="600" cy="97" r="3.5" fill="#059669" />
      <circle cx="558" cy="55" r="2.5" fill="#3B82F6" />
    </g>

    <!-- Rotating Logo Image -->
    <g class="logo-image-group">
      <image href="data:image/png;base64,{logo_b64}" xlink:href="data:image/png;base64,{logo_b64}" x="570" y="25" width="60" height="60" />
    </g>
  </g>

  <g transform="translate(320, 0)">
    <!-- Protocol Status Badge with Subtle Binary -->
    <g transform="translate(125, 106)">
      <rect class="cyber-badge" x="0" y="0" width="310" height="24" rx="12" fill="rgba(29, 185, 84, 0.12)" stroke="#1DB954" stroke-opacity="0.4" />
      <circle cx="14" cy="12" r="3.5" fill="#1DB954" />
      <text x="26" y="16" font-family="'Fira Code', monospace" font-size="11" font-weight="700" fill="#A7F3D0">
        SYSTEM.DECODE // 01000101 01010000
      </text>
    </g>

    <!-- Main Title Name with Animated Glow -->
    <text x="280" y="172" class="animated-title" text-anchor="middle" font-family="'Inter', 'Segoe UI', sans-serif" font-weight="900" font-size="46" letter-spacing="6" fill="#FFFFFF">
      EPUN MANULA
    </text>

    <!-- Subtitle Line -->
    <text x="280" y="206" text-anchor="middle" font-family="'Fira Code', monospace" font-weight="700" font-size="14" letter-spacing="2" fill="#1DB954">
      SOFTWARE ENGINEER • FULL-STACK DEVELOPER • TECH ENTREPRENEUR
    </text>

    <!-- CENTER BOTTOM WEBSITE & EMAIL PILL BAR -->
    <g transform="translate(0, 236)">
      <rect x="0" y="0" width="560" height="52" rx="26" fill="rgba(0, 0, 0, 0.75)" stroke="url(#emerald-glow)" stroke-width="1.8" />
      
      <!-- Website Pill Section -->
      <g transform="translate(35, 14)">
        <circle cx="12" cy="12" r="5" fill="#1DB954" />
        <text x="26" y="17" font-family="'Fira Code', monospace" font-size="15" font-weight="700" fill="#FFFFFF">
          epunmanula.com
        </text>
      </g>

      <!-- Separator Dot -->
      <text x="265" y="31" text-anchor="middle" font-family="'Fira Code', monospace" font-size="16" font-weight="700" fill="#1DB954">•</text>

      <!-- Email Pill Section -->
      <g transform="translate(305, 14)">
        <circle cx="12" cy="12" r="5" fill="#10B981" />
        <text x="26" y="17" font-family="'Fira Code', monospace" font-size="15" font-weight="700" fill="#1DB954">
          dev@epunmanula.com
        </text>
      </g>
    </g>
  </g>

  <!-- RIGHT SIDE TECH STACK ICONS (Compact Grid - No Text Names) -->
  <!-- 7. WEBASSEMBLY LOGO -->
  <g transform="translate(1040, 55)">
    <rect x="0" y="0" width="40" height="40" rx="10" fill="#654FF0" stroke="#FFFFFF" stroke-width="1.2" />
    <text x="20" y="26" text-anchor="middle" font-family="'Fira Code', monospace" font-weight="900" font-size="13" fill="#FFFFFF">WA</text>
  </g>

  <!-- 8. SUPABASE LOGO -->
  <g transform="translate(1100, 55)">
    <circle cx="20" cy="20" r="20" fill="rgba(10, 15, 25, 0.85)" stroke="#3ECF8E" stroke-width="1.5" />
    <path d="M 22 9 L 11 22 L 19 22 L 18 31 L 29 18 L 21 18 Z" fill="#3ECF8E" />
  </g>

  <!-- 9. DOCKER LOGO -->
  <g transform="translate(1040, 140)">
    <circle cx="20" cy="20" r="20" fill="rgba(10, 15, 25, 0.85)" stroke="#2496ED" stroke-width="1.5" />
    <g transform="translate(9, 13) scale(0.6)">
      <rect x="0" y="12" width="6" height="5" rx="1" fill="#2496ED" />
      <rect x="8" y="12" width="6" height="5" rx="1" fill="#2496ED" />
      <rect x="16" y="12" width="6" height="5" rx="1" fill="#2496ED" />
      <rect x="8" y="5" width="6" height="5" rx="1" fill="#2496ED" />
      <rect x="16" y="5" width="6" height="5" rx="1" fill="#2496ED" />
      <path d="M 0 20 C 5 20 8 26 22 26 C 30 26 36 20 36 20" fill="none" stroke="#2496ED" stroke-width="2" />
    </g>
  </g>

  <!-- 10. GIT LOGO -->
  <g transform="translate(1100, 140)">
    <g transform="translate(20, 20) rotate(45)">
      <rect x="-14" y="-14" width="28" height="28" rx="8" fill="#F05032" stroke="#FFFFFF" stroke-width="1.2" />
    </g>
    <g transform="translate(9, 9) scale(0.65)">
      <circle cx="12" cy="8" r="3" fill="#FFFFFF" />
      <circle cx="12" cy="26" r="3" fill="#FFFFFF" />
      <circle cx="24" cy="18" r="3" fill="#FFFFFF" />
      <path d="M 12 11 L 12 23 M 12 14 Q 20 14 24 15" stroke="#FFFFFF" stroke-width="2.5" fill="none" />
    </g>
  </g>

  <!-- 11. AWS LOGO -->
  <g transform="translate(1040, 225)">
    <circle cx="20" cy="20" r="20" fill="rgba(10, 15, 25, 0.85)" stroke="#FF9900" stroke-width="1.5" />
    <text x="20" y="25" text-anchor="middle" font-family="'Inter', sans-serif" font-weight="900" font-size="11" fill="#FF9900">AWS</text>
  </g>

  <!-- 12. TAILWIND LOGO -->
  <g transform="translate(1100, 225)">
    <circle cx="20" cy="20" r="20" fill="rgba(10, 15, 25, 0.85)" stroke="#06B6D4" stroke-width="1.5" />
    <path d="M 10 19 C 12 13 16 13 18 15 C 20 17 22 19 26 19 C 30 19 32 15 32 15 C 30 21 26 21 24 19 C 22 17 20 15 16 15 C 12 15 10 19 10 19 Z" fill="#06B6D4" />
  </g>
</svg>
'''

with open(out_path_1, "w", encoding="utf-8") as f:
    f.write(svg_template)

if os.path.exists(os.path.dirname(out_path_2)):
    with open(out_path_2, "w", encoding="utf-8") as f:
        f.write(svg_template)

print("Animated SVG banner generated successfully!")
