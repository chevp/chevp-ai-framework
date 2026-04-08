---
name: Cross-Platform
description: Every repo that targets desktop must also target Android from day one — retrofit is not an option
type: guideline
---

# Guideline: Cross-Platform

**Rule:** If a project declares more than one platform target (e.g. desktop + Android), every commit must build and pass on **all** declared targets. Platform parity is enforced from the first commit, not retrofitted later.

**Why:** Retrofitting mobile support onto a desktop-first codebase is exponentially more expensive than building for both from the start. Desktop-only assumptions (filesystem paths, unlimited RAM, persistent GL context, mouse input, synchronous I/O on main thread) silently embed themselves throughout the codebase. Each one becomes a hidden migration cost that compounds over time. By the point someone says "now let's port to Android", the cost is no longer a port — it's a rewrite.

**How to apply:** When a project's `platform-targets.md` declares multiple platforms, the AI enforces platform parity at every lifecycle step — Context checks for platform-specific assumptions, Exploration plans must cover all targets, Production code must build on all targets. The AI blocks any change that introduces a platform-specific dependency without a PAL (Platform Abstraction Layer) boundary.

## Platform-Specific Assumptions the AI Must Catch

The AI must flag code or plans that rely on any of these without a platform abstraction:

### File System / Storage
- Direct filesystem paths (`std::filesystem::path`, `fopen`, hardcoded paths)
- Android uses Scoped Storage and `AAssetManager` — no real filesystem access for assets
- Hardcoded path separators or drive letters

### Memory / Resources
- Assuming >4 GB RAM available (mobile processes often get 512 MB–1 GB)
- Loading full-resolution textures without LOD / streaming strategy
- No asset budget or bundle size constraint

### Graphics / Rendering
- Desktop-only Vulkan features (wide subgroup ops, `glMultiDrawIndirect`, unconstrained MSAA)
- Assuming GL context is persistent (Android can destroy it on background/rotate)
- Texture formats without mobile variants (BC7 without ASTC fallback)
- Shader precision assumptions (`highp` everywhere without `mediump` consideration)

### Input
- Mouse/keyboard coordinates hardcoded without touch abstraction
- No consideration for screen rotation, soft keyboard, or gesture navigation
- Window resize vs. Android surface recreation

### Threading / Lifecycle
- Synchronous I/O on main thread (causes ANR on Android)
- Assuming the app runs continuously (Android pauses/resumes/destroys)
- No handling of activity lifecycle (`onPause`, `onResume`, `onDestroy`)

### Build / Distribution
- Binary size unconstrained (Play Store limits: 150 MB APK, 2 GB with asset packs)
- Native dependencies only compiled for x86_64 (missing arm64-v8a)
- No Gradle/NDK build path alongside CMake/MSVC

## Platform Abstraction Layer (PAL)

Platform-specific code must be isolated behind abstraction boundaries:

```
core/           ← platform-agnostic, references only PAL interfaces
pal/            ← interface definitions
pal/desktop/    ← desktop implementations
pal/android/    ← Android implementations
```

**Rules:**
- `core/` must never import platform headers directly (`<windows.h>`, `<android/asset_manager.h>`, etc.)
- Every platform-specific operation goes through a PAL interface
- PAL interfaces live in a neutral location, implementations are compile-time selected
- A new PAL interface requires an ADR

## Asset Dual-Target Rule

When a project targets desktop + Android, assets must be produced for both:

| Asset Type | Desktop Format | Android Format |
|-----------|---------------|----------------|
| Textures | BC7 / DXT | ASTC / ETC2 |
| Shaders | SPIR-V (desktop Vulkan) | SPIR-V (mobile Vulkan) or GLSL ES |
| Models | Full LOD chain | Reduced LOD + streaming |
| Bundles | No size limit | Budget per asset pack |

An asset pipeline that only outputs one format is a gate violation.

## Gate Integration

This guideline extends the quality gates when `platform-targets.md` exists:

| Gate | Additional Criteria |
|------|-------------------|
| **G1** | Platform targets declared, PAL boundary identified, asset format strategy documented |
| **G2** | Plan covers all targets, no single-platform design, prototype validated on all targets (or justified skip) |
| **G3** | Build passes on all declared targets, no platform-specific code outside PAL, asset pipeline outputs all formats |

## AI Behavior

### MUST
- Read `platform-targets.md` (if it exists) before any architecture or code work
- Flag platform-specific assumptions in plans and code
- Require PAL boundaries for platform-specific operations
- Verify builds target all declared platforms
- Catch single-format asset pipelines

### MUST NOT
- Allow "we'll add Android later" as a plan — if the target is declared, it ships together
- Silently accept desktop-only dependencies in core code
- Skip mobile build verification in Production
- Approve plans that only describe the desktop path

## Anti-Patterns

| Anti-Pattern | Why It Breaks Parity |
|-------------|---------------------|
| "Android build is broken but desktop works, ship it" | Parity is a gate — both must pass |
| `#ifdef ANDROID` scattered through core code | Platform logic belongs in PAL, not in business logic |
| "We'll optimize for mobile later" | Performance assumptions compound — budget from day one |
| Asset pipeline only outputs BC7 | Android has no BC7 support — ASTC must be produced alongside |
| Testing only on desktop emulator | Android device/emulator must be in CI or local test loop |
