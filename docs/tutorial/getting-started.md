# Getting started

This page covers starting Pygacq, an overview of the main window, and the keys
and mouse actions in the image viewer. The pages that follow walk through one
example acquisition of each mode.

## Starting Pygacq

:::{note}
These startup instructions apply during the testing and transition period, while Pygacq
runs on the control room development machine.
:::

Pygacq runs on the development machine of each site:

| Site         | Machine                  |
|--------------|--------------------------|
| Gemini North | `telops@hbftelops-ld3`   |
| Gemini South | `telops@sbftopsdev-ld1`  |

### Daytime testing

Work directly on the development machine in the control room, or connect to it
via Keeper.

1. Go to the Pygacq base directory:

   ```bash
   cd ~/Scratch/pygacq_test/
   ```

2. Run the startup script. It sets up the Pygacq environment and pulls the
   latest version from GitHub:

   ```bash
   source pygacq-activate.sh
   ```

3. Start Pygacq in day mode:

   ```bash
   pygacq -d
   ```

### Nighttime observing

1. From the observer's machine, log in to the development machine:

   - Gemini North:

     ```bash
     ssh telops@hbftelops-ld3
     ```

   - Gemini South:

     ```bash
     ssh -XY telops@sbftopsdev-ld1
     ```

2. Go to the Pygacq base directory and run the startup script:

   ```bash
   cd ~/Scratch/pygacq_test/
   source pygacq-activate.sh
   ```

3. Start Pygacq in night mode:

   ```bash
   pygacq
   ```

:::{important}
Run the startup script at the beginning of each night. Pygacq is updated
daily, and the script pulls in the latest changes.
:::

### Day mode and night mode

|                                 | Day mode (`pygacq -d`)        | Night mode (`pygacq`)  |
|---------------------------------|-------------------------------|------------------------|
| Offsets                         | never sent                    | can be sent            |
| Images are read from            | dataflow                      | perm                   |
| Cache and measurements database | deleted when Pygacq closes    | kept                   |
| Window title                    | **Pygacq - Daytime Mode**     | **Pygacq**             |

In day mode each Pygacq session works in its own temporary directory, which
holds its cache and its measurements database. Several people can therefore
test Pygacq at the same time without getting in each other's way. The
directory is deleted when Pygacq closes, to save disk space.


### Configuration

Pygacq reads its settings from a `~/.config/pygacq/config.toml` file. It sets
the observatory site and the directories Pygacq uses: where to find images,
MDFs and finder charts, and where to keep its cache and measurements database.
Most observers never need to change it.

One of these directories is the **user data directory** (`USER_DATA_DIRECTORY`
in the config file). It is the place to put your own files for Pygacq to
find: acquisition, sky and slit images, MDFs and MOS coordinate files. When
you type an image number or a file name, Pygacq looks in this directory as
well as in the usual data and MDF directories. The **User Dir** button in
the **File Browser** tab takes you there.

### Clearing the cache and the database

Pygacq remembers the acquisitions it has already run:

- the **cache** keeps the images it has loaded and processed, so that it
  doesn't have to process them again;
- the **measurements database** keeps the measurements and offsets of earlier
  acquisitions, such as slit and MOS box positions, so that later
  acquisitions of the same observation can reuse them.

To run an acquisition as if it had never been run before, with freshly
processed images and no reused measurements, clear both: choose
**File → Cleanup → Reset Cache**, then **File → Cleanup → Reset Database**.

## The main window at a glance

:::{figure} images/main-window.png
:width: 100%
:alt: The Pygacq main window with a GMOS long-slit acquisition loaded

The Pygacq main window.
:::

The window has three columns. From left to right: information about the image,
the image viewer, and the acquisition panel. This section is a brief overview;
each part is described in [The main window in detail](main-window.md).

### Left column: image information and log

The upper part has four tabs:

**Analysis**
: Plots and fits for the point under the cursor, such as the radial profile you
  get when you press {kbd}`R` over a star. Each plot has its parameters above
  it and its results below.

  :::{tip}
  The analysis keys ({kbd}`R`, {kbd}`L`, {kbd}`J`, {kbd}`C`, {kbd}`K`,
  {kbd}`E`, {kbd}`A`, {kbd}`S`, {kbd}`V`) work at any moment: before, during
  and after an acquisition, and in any step.
  :::

  :::{figure} images/analysis-tab.png
  :width: 60%
  :alt: The Analysis tab with a line fit, its parameters and results

  The line fit plot: parameters at the top, plot, and results.
  :::

**Image Header** and **Image Info**
: The FITS header and a summary of the image shown in the viewer. Click an
  image in the **Acquisitions** list to see those of that image instead.

**Finder Charts**
: The finder charts for the target. The list button shows all the charts of
  the program.

Below the tabs, **Pygacq Log** shows what Pygacq is doing. Look here first if
something does not behave as you expect.

More: [Left column](main-window.md#left-column-image-information-and-log).

### Middle column: the image viewer

#### Viewer tabs

The viewer has three tabs: **Acquisition Image** (the image being acquired),
**Catalog Image** (a sky survey image of the field) and **Other Image** (any
other image you want to look at).

Above the tabs, choosing a survey in the **Image Server** menu loads its image
into the **Catalog Image** tab, and choosing a catalog in the **Catalog
Server** menu overlays it on the **Acquisition Image** (not available yet). Other buttons above the tabs open another image, match it to the
acquisition image by WCS or pixels, show both side by side, or blink between
them.

#### Display controls

Under the image are **Stretching**, the **Cut Low** and **Cut High** levels,
and **Show overlays** (**Compass**, **Saturation**). At the bottom, the toolbar
zooms, rotates and flips the image.

In the image:

- left-drag moves the image, middle-click centres it on the point clicked, and
  right-drag changes the contrast and brightness;
- {kbd}`H` over a bright part and {kbd}`O` over a dark part set the cut levels
  from the pixel under the cursor.


More: [Middle column](main-window.md#middle-column-the-image-viewer).

### Changing the image orientation

To rotate or flip the acquisition image, for example to match a finder chart,
use the nine buttons at the right end of the toolbar under the viewer. Hover
the cursor over a button to see what it does.

From left to right:

| Icon                                         | Button              | What it does                                                                |
|----------------------------------------------|---------------------|-----------------------------------------------------------------------------|
| ![](images/icons/flip_x.svg){w=24px}         | Flip X              | Flip the image left–right                                                   |
| ![](images/icons/flip_y.svg){w=24px}         | Flip Y              | Flip the image up–down                                                      |
| ![](images/icons/swap_xy.svg){w=24px}        | Swap XY             | Swap the X and Y axes                                                       |
| ![](images/icons/rotate.svg){w=24px}         | Rotate              | While on, left-drag in the image to rotate it; right-click to go back to 0° |
| ![](images/icons/rot90ccw.svg){w=24px}       | Rotate 90°          | Rotate the image by 90°                                                     |
| ![](images/icons/rot90cw.svg){w=24px}        | Rotate −90°         | Rotate the image by −90°                                                    |
| ![](images/icons/orient_nw.svg){w=24px}      | Orient N=Up E=Right | Rotate and flip the image so that North is up and East is right             |
| ![](images/icons/orient_ne.svg){w=24px}      | Orient N=Up E=Left  | Rotate and flip the image so that North is up and East is left              |
| ![](images/icons/reset_rotation.svg){w=24px} | Reset               | Undo all flips and rotations (the last button on the right)                 |


More: [The toolbar](main-window.md#the-toolbar).

### Right column: the acquisition panel

#### Acquisition list

At the top, **Acquisitions** lists the current acquisition and the ones
already done, with their images, and **File Browser** lets you browse for
images.

Below that:

- a text box, *Enter image number*, where you type the image to acquire;
- **Start** starts an acquisition and **Abort** stops it;
- **Auto Start** starts an acquisition automatically whenever a new
  acquisition image arrives (not available yet);
- **Slit**, **Sky** and **MDF** are normally left on **Auto**. Choose **User**
  to pick the image or file yourself.

:::{tip}
To choose the sky or slit image, set **Sky** or **Slit** to **User**, then
tick the **Sky** or **Slit** box of the image you want in the
**Acquisitions** list. Pygacq checks that the image is suitable before
using it.
:::

:::{figure} images/user-sky-slit.png
:width: 60%
:alt: Slit and Sky set to User, with the slit and sky images ticked in the Acquisitions list

**Slit** and **Sky** set to **User**, with the slit and sky images ticked in
the list.
:::

#### Current Acquisition

:::{important}
**Current Acquisition** is the part of the window you work with during an
acquisition. It changes at every step: it tells you what Pygacq has found, what
to check, and what to do next, and it waits for you to act. Keep an eye on it
until the acquisition is finished.
:::

The **Current Acquisition** tab takes you through the acquisition one step at a
time. Its row of step buttons (for long-slit: **Mark target(s)**, **Confirm
slit center**, then **Send offsets**) shows where you are. For each step it
shows:

- a status box saying what Pygacq has found or expects, e.g. that the slit was
  traced or that the target has to be marked;
- the choices and buttons for the step, e.g. **Accept** or **Remeasure slit**;
- the instructions, listing the keys you can use in the image for this step.

At the end it shows the calculated offsets with advice on whether to send them.

:::{figure} images/acquisition-guide.png
:width: 50%
:alt: The Current Acquisition tab of a Flamingos-2 long-slit acquisition at the Mark target(s) step, with the Blind Offset flag

The **Current Acquisition** tab at the **Mark target(s)** step. The red
**Blind Offset** flag means Pygacq treats this as a blind-offset acquisition
and adjusts the offset advice to it.
:::

:::{tip}
During an acquisition you can move back and forth between the steps: click the
button of an earlier step to go back to it, for example to check or correct
the target you marked, and then continue from there.
:::

More: [Right column](main-window.md#right-column-the-acquisition-panel).


## Keys and mouse in the image viewer

Keys act on the point under the mouse cursor in the image viewer.

These keys show a plot or fit in the **Analysis** tab. They work at any time,
even when no acquisition is running, on the **Acquisition Image** and on the
**Other Image** tab:

| Key          | Action                                                    |
|--------------|-----------------------------------------------------------|
| {kbd}`R`     | Radial profile and centroid, with a contour plot          |
| {kbd}`L`     | Line (row) plot                                           |
| {kbd}`J`     | Line (row) fit                                            |
| {kbd}`C`     | Column plot                                               |
| {kbd}`K`     | Column fit                                                |
| {kbd}`E`     | Contour plot                                              |
| {kbd}`A`     | Aperture photometry                                       |
| {kbd}`S`     | Surface plot                                              |
| {kbd}`V`     | Cut plot: press once at the start and once at the end     |

These keys only work during an acquisition, on the acquisition image:

| Key                          | Action                                                         |
|------------------------------|----------------------------------------------------------------|
| {kbd}`X`                     | Mark the exact position under the cursor                       |
| {kbd}`Q` or {kbd}`Enter`     | Accept, same as the highlighted button in **Current Acquisition** |

These keys and mouse actions change the display:

| Key or mouse                 | Action                                                         |
|------------------------------|----------------------------------------------------------------|
| {kbd}`H`                     | Set **Cut High** to the value of the pixel under the cursor    |
| {kbd}`O`                     | Set **Cut Low** to the value of the pixel under the cursor     |
| Arrow keys                   | Move the cursor by one screen pixel                            |
| Left-drag                    | Move the image around                                          |
| Middle-click                 | Centre the view on the clicked point                           |
| Right-drag                   | Change contrast (up/down) and brightness (left/right)          |

:::{note}
Each acquisition step has its own set of keys, for example to mark the target,
trace the slit or mark the boxes of a MOS mask. The keys for the current step
are listed in its **INSTRUCTIONS** in the **Current Acquisition** tab.
:::
