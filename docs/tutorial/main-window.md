# The main window in detail

This page describes each part of the Pygacq main window in detail. For a brief
overview, see [The main window at a glance](getting-started.md#the-main-window-at-a-glance).

:::{figure} images/main-window.png
:width: 100%
:alt: The Pygacq main window with a GMOS long-slit acquisition loaded

The Pygacq main window.
:::

The window has three columns. From left to right: information about the image,
the image viewer, and the acquisition panel.

## Left column: image information and log

The upper part of the column has four tabs: **Analysis**, **Image Header**,
**Image Info** and **Finder Charts**. Below them, **Pygacq Log**
shows what Pygacq is doing. Look there first if something does not behave as
you expect.

### Image Header and Image Info

**Image Header** lists the full FITS header of an image: the primary header and
the headers of all extensions, so per-extension keywords such as `DETSEC` are
there too. Type in the **Filter** box to show only the header lines containing
that text, e.g. `EXPTIME`.

**Image Info** shows a summary of the same image: file name and original name,
path, object, RA and Dec, instrument, observation ID, datalabel, camera, filter,
disperser, focal plane mask, coadds, ISS port, image size and binning.

Both tabs show one of two images:

- **The image in the viewer.** During an acquisition, the tabs show the header
  and information of the **processed** image, which is the image you see in the
  viewer.
- **An image you click in the Acquisitions list.** Click any image in the
  **Acquisitions** list (see
  [Right column](#right-column-the-acquisition-panel)) to show its header and
  info, even if it isn't displayed in the viewer. This is a quick way to check,
  for example, the filter or exposure time of the sky or slit image.

### Finder Charts

When an acquisition starts, Pygacq looks for finder charts in the program's
directory, matching the files to the target name:

- If one or more charts match, the first one is shown. With several matching
  charts, a button for each one appears below the chart; click one to show it.
  Use the mouse wheel over the chart, or the zoom buttons below it, to zoom in
  and out, and the expand button
  to give the chart more room.
- If no chart matches the target name, the tab shows the list of files instead
  (see below).

To see **all** the finder charts of the program, click the list button (tooltip
*Show all finding charts*). The tab then lists every chart file in the
program's directory, with the target name, RA and Dec at the top. Double-click a
file to display it. This is useful when the charts are not named after the
target. Click the list button again to go back to the chart.

:::{figure} images/finder-charts-list.png
:width: 40%
:alt: The Finder Charts tab listing all chart files of the program, with the target name, RA and Dec at the top

The list of all finder charts of the program.
:::

:::{note}
Proposal, summary and attachment files are left out of the list.
:::

:::{warning}
If the target is a blind-offset star, the list starts with *Object is an
offset star! Unable to identify finding chart for the primary target!* The
charts in the program directory show the primary target, not the star in your
acquisition image.
:::

### Analysis

The **Analysis** tab shows the plots and fits you get with the analysis keys:
{kbd}`R`, {kbd}`L`, {kbd}`J`, {kbd}`C`, {kbd}`K`, {kbd}`E`, {kbd}`A`, {kbd}`S`
and {kbd}`V` (see [Keys and mouse in the image viewer](getting-started.md#keys-and-mouse-in-the-image-viewer)).
Each key has its own page, shown when you press the key over an image. For a
reminder of the keys, click the small {guilabel}`i` button at the top right of
the tab.

:::{tip}
The analysis keys work at any moment: before, during and after an
acquisition, and in any step.
:::

Each page has three parts:

**Parameters**
: A section at the top, e.g. **Radial Profile Parameters** or **Line Fit
  Parameters**, with the settings for that plot or fit. Click its title to open
  or close it. After changing a value, click **Recompute** to redo the plot at
  the same position. **Default** puts the settings back to their defaults.

**Plot**
: The plot itself, with a small toolbar underneath to zoom, pan or save it.

**Results**
: The numbers measured, below the plot.

:::{figure} images/analysis-tab.png
:width: 60%
:alt: The Analysis tab with a line fit, its parameters and results

The line fit plot: parameters at the top, plot, and results.
:::

For example, the radial profile ({kbd}`R`) page has:

- in **Radial Profile Parameters**: the fit type (*moffat* or *gaussian*),
  whether to fit and subtract the background, the radius, sky buffer and sky
  radius, the plotting radius, and the **Centering** method (*IRAF marginal* by
  default, or *2D Gaussian*, *2D Gaussian (robust)*, *CoM*, *No centering*) with
  its centering box. There is also a **Contour Parameters** section, since
  {kbd}`R` shows a contour plot of the star as well.
- in **Results**: **Center X** and **Center Y**, **FWHM fit** (pixels),
  **Star size** (FWHM in arcseconds), **Sky**, **Peak**, **Flux**, **Mag** and
  **Ellipticity**.

:::{tip}
The **Centering** method is what Pygacq uses to find the centre of the target
when you press {kbd}`R` while marking it. If the centroid lands in the wrong
place, for example on a faint or extended target, try a different method and
click **Recompute**. Or mark the target with {kbd}`X` instead.
:::

The other pages work the same way. Their **Results** show, for example, the
centre, peak, FWHM and background of a line or column fit ({kbd}`J`, {kbd}`K`),
or the flux, sky per pixel and magnitude from aperture photometry ({kbd}`A`).

## Middle column: the image viewer

### Viewer tabs

The viewer has three tabs: **Acquisition Image** (the image being acquired),
**Catalog Image** (a sky survey image of the field) and **Other Image** (any
other image you want to look at).

Above the tabs, choosing a survey in the **Image Server** menu loads its image
into the **Catalog Image** tab, and choosing a catalog in the **Catalog
Server** menu overlays it on the **Acquisition Image** (not available yet). Other buttons above the tabs open another image, match it to the
acquisition image, show both side by side, or blink between them (see
[Looking at another image](#looking-at-another-image)).

When an acquisition starts, the view is centred on the *nominal position*: the
place in the image where the target should end up.

### Display controls

Under the image:

- **Stretching** selects how pixel values are mapped to brightness: *linear*,
  *log*, *power*, *sqrt*, *squared*, *asinh*, *sinh* or *histeq*.
- **Cut Low** / **Cut High** are the pixel values shown as black and white.
  Type them and press {kbd}`Enter` or click **Set Levels**; **Auto Levels**
  picks them for you. You can also set them from the image with {kbd}`O` and
  {kbd}`H` (see [below](#setting-the-cut-levels-from-the-image)).
- **Show overlays** turns on and off what Pygacq draws on the image:
  - **Compass**: the orientation of the image on the sky;
  - **Saturation**: marks saturated pixels in red;
  - **All overlays**: turns everything on or off at once.

At the bottom of the column, the [toolbar](#the-toolbar) zooms, rotates and
flips the image.

### Moving around the image

In the viewer:

- **Left-drag** (hold the left button and move the mouse) moves the image
  around.
- **Middle-click** centres the view on the point you clicked.
- **Right-drag** changes the contrast and brightness: move up and down to
  change the contrast, left and right to change the brightness. Setting the cut
  levels, or **Auto Levels**, puts them back to normal.
- The **arrow keys** move the cursor by one screen pixel. This is handy to put
  the cursor exactly where you want before pressing {kbd}`X`.

<!-- TODO: these bindings are what works on Linux. Say what differs on macOS
     (e.g. trackpad scrolling), if observers use it. -->

### Setting the cut levels from the image

The quickest way to get a good display is to take the cut levels from the image
itself:

- Put the cursor on the **brightest** part you want to see, e.g. the peak of
  the target, and press {kbd}`H`. The value of that pixel becomes **Cut High**:
  anything brighter is shown as white.
- Put the cursor on the **darkest** part you want to see, e.g. the sky
  background, and press {kbd}`O`. The value of that pixel becomes **Cut Low**:
  anything darker is shown as black.

The **Cut High** and **Cut Low** boxes are updated, so you can fine-tune the
values there.

### The toolbar

The toolbar at the bottom of the column acts on the image in the viewer.
Hover over a button to see its name. From left to right:

| Icon                                         | Button              | What it does |
|----------------------------------------------|---------------------|--------------|
| ![](images/icons/ruler.svg){w=24px}          | Ruler               | Measure distances: drag between two points (left-drag doesn't move the image while the ruler is on) |
| ![](images/icons/sqrt.svg){w=24px}           | Color distribution  | While on, scroll over the image to change the stretching |
| ![](images/icons/palette.svg){w=24px}        | Color map           | While on, scroll over the image to change the color map |
| ![](images/icons/auto_cuts.svg){w=24px}      | Auto cut levels     | Same as **Auto Levels** |
| ![](images/icons/reset_contrast.svg){w=24px} | Reset contrast      | Undo contrast and brightness changes made by right-dragging |
| ![](images/icons/zoom_in.svg){w=24px}        | Zoom in             | Zoom in |
| ![](images/icons/zoom_out.svg){w=24px}       | Zoom out            | Zoom out |
| ![](images/icons/zoom_fit.svg){w=24px}       | Zoom to fit         | Fit the whole image in the viewer |
| ![](images/icons/zoom_100.svg){w=24px}       | Zoom 1:1            | One image pixel per screen pixel |
| ![](images/icons/center_image.svg){w=24px}   | Center image        | Centre the image in the viewer |
| ![](images/icons/flip_x.svg){w=24px}         | Flip X              | Flip the image left–right |
| ![](images/icons/flip_y.svg){w=24px}         | Flip Y              | Flip the image up–down |
| ![](images/icons/swap_xy.svg){w=24px}        | Swap XY             | Swap the X and Y axes |
| ![](images/icons/rotate.svg){w=24px}         | Rotate              | While on, left-drag in the image to rotate it; right-click to go back to 0° |
| ![](images/icons/rot90ccw.svg){w=24px}       | Rotate 90°          | Rotate the image by 90° |
| ![](images/icons/rot90cw.svg){w=24px}        | Rotate −90°         | Rotate the image by −90° |
| ![](images/icons/orient_nw.svg){w=24px}      | Orient N=Up E=Right | Rotate and flip the image so that North is up and East is right |
| ![](images/icons/orient_ne.svg){w=24px}      | Orient N=Up E=Left  | Rotate and flip the image so that North is up and East is left |
| ![](images/icons/reset_rotation.svg){w=24px} | Reset               | Undo all flips and rotations |

The last nine buttons, from **Flip X** to **Reset**, change the orientation of
the image, for example to match a finder chart. Most finder charts have North
up and East left, so **Orient N=Up E=Left** is usually the quickest way to
match one.


### Looking at another image

Besides the acquisition image, you can open any other FITS image in the
**Other Image** tab, e.g. an earlier acquisition image of the same target. The
buttons above the viewer tabs work with it:

**Open image in new frame**
: Choose a FITS file; it opens in the **Other Image** tab. The analysis keys
  ({kbd}`R`, {kbd}`L`, {kbd}`A`, …) work on this image too. The acquisition
  keys ({kbd}`X`, {kbd}`Q`) don't: you can only mark the target on the
  acquisition image.

**Match**
: Keep the other viewers in step with the **Acquisition Image**, so when you
  pan, zoom or rotate one, the others follow:
  - **WCS**: match by sky coordinates. The same point on the sky stays at the
    same place in both viewers, even if the images have different pixel
    scales or orientations.
  - **Image**: match by pixel coordinates. Use this for images without a
    usable WCS, or taken with the same setup.
  - **none**: each viewer moves on its own.

**Grid View**
: Show the **Acquisition Image** and a second image side by side, instead of
  in tabs. The second image is the **Other Image** tab if that is the tab you
  were looking at, otherwise the **Catalog Image**. The image panel is expanded
  to make room. When the second image is the **Catalog Image**, matching by
  **WCS** is turned on. Click an image to make it the active one; it gets a
  blue border. Click **Grid View** again to go back to tabs.

**Blink Frames**
: Switch back and forth between the **Acquisition Image** and the **Other
  Image** tab, to spot differences between the two. Combine it with **Match**
  so both images show the same area. Click again to stop.

**Expand View Panel**
: Hide the side columns to give the image as much room as possible. Click again
  to bring them back.

:::{figure} images/grid-view.png
:width: 100%
:alt: Grid view with the acquisition image and a second image side by side, matched by WCS

**Grid View** with **Match** set to **WCS**: the **Acquisition Image** (left,
active) and a second image of the same field.
:::

## Right column: the acquisition panel

### Acquisition list

At the top are two tabs: **Acquisitions** lists the current acquisition and the
ones already done, with their images, and **File Browser** lets you browse the
data directories for images (see [File Browser](#file-browser)).

The **Acquisitions** list groups the images by observation. For each
image it shows the step, the P and Q offsets, the focal plane mask, and three
tick boxes: **Src** (the acquisition image), **Slit** and **Sky** (the slit
and sky images used). Click an image to see its header and info in the left
column (see [Image Header and Image Info](#image-header-and-image-info)).

Below that:

- A text box, *Enter image number*, where you type the image to acquire, and
  next to it the button that opens the
  [acquisition options](#acquisition-options).
- **Start** starts an acquisition (see
  [Starting an acquisition](#starting-an-acquisition)).
- **Auto Start** starts an acquisition automatically whenever a new acquisition
  image arrives (not available yet).
- **Abort** stops the ongoing acquisition.
- **Slit**, **Sky** and **MDF**: which slit image, sky image and mask definition
  file to use (see
  [Choosing the slit and sky images yourself](#choosing-the-slit-and-sky-images-yourself)).

#### Starting an acquisition

There are several ways to start an acquisition:

**Type the image**
: In the *Enter image number* box, type the full file name, e.g.
  `N20260804S0001`, or just the image number, e.g. `40`, for one of tonight's
  images. Then press {kbd}`Enter` or click **Start**.

**Pick an image in the Acquisitions list**
: Double-click an image, or select it and click **Start**. This is the quickest
  way to run an earlier acquisition again.

**Pick a file in the File Browser**
: Double-click a FITS file, or select it and click **Start**.

**Auto Start**
: Pygacq starts an acquisition by itself when a new acquisition image arrives (not available yet).


#### Select Acquisition Type dialog

Pygacq usually works out the type of acquisition by itself: from the image,
from earlier measurements of the same observation, from the mask in the beam
or from the slit image. The **Select Acquisition Type** dialog opens when you
need to decide:

- Pygacq can't work out the type;
- a MOS mask is in the beam but its MDF can't be found. The dialog then opens
  with **MOS** already selected;
- the **Manual acquisition type** option is ticked (see
  [Acquisition options](#acquisition-options));
- **MDF** is set to **User** but no file is given, on an image with the MOS mask
  in the beam.

:::{figure} images/acquisition-type-dialog.png
:width: 60%
:alt: The Select Acquisition Type dialog with MOS selected

The **Select Acquisition Type** dialog with **MOS** selected.
:::

The dialog only offers the types the instrument supports. Choose one, fill in
what it needs, and click **Select**. **Abort** cancels starting the
acquisition.

**Imaging**
: Nothing else is needed.

**Long-slit**
: Specify the slit image:
  - **Auto-detect**: Pygacq finds the slit image among the images of the
    observation.
  - **Slit image number, or full path**: type it, or click **Browse**.
  - **No-slit acquisition (use default slit position)**: acquire without a slit
    image, using the default slit position (not available yet).

**MOS**
: Specify the mask:
  - **Mask number**: the program part of the mask name is filled in; type the
    mask number after the dash.
  - **MDF or Coordinate file**: type the path, or click **Browse**.
  - **Create coo file from MOS image** (GMOS only): mark the alignment
    boxes on the mask-in image by hand, to create a coordinates file for a mask
    that has no, or bad, MDF.

**IFU**
: Choose the IFU mode. For GMOS, **IFU-2** and **IFU-R** are shown; click
  **More IFU options** for **IFU-B** and the **Nod and Shuffle** modes. For
  GNIRS there is a single **IFU** choice.

**Select** stays greyed out until the choice is complete, for example until the
mask number or file points to a valid MDF or coordinates file. A message under
the field says what is wrong, e.g. that the file doesn't exist.

#### File Browser

The **File Browser** tab lists the files and folders of one directory. It
opens in the user data directory.

- Double-click a folder to open it, or **..** to go up one level. Double-click
  a FITS file to start an acquisition from it.
- The list refreshes by itself every second while the tab is shown, so new
  images appear as they arrive. **Refresh** updates it straight away.
- **User Dir** goes to the user data directory, where you can put your own
  files for Pygacq to find (see
  [Configuration](getting-started.md#configuration)).
- **Data Dir** goes to the data directory: dataflow in day mode, perm at night.
  It shows only tonight's images, newest first.

The box under the list shows the current folder, or the file you selected. You
can also type a path there and press {kbd}`Enter` or click **Load**: a folder
opens in the list, and a file starts an acquisition.

:::{figure} images/file-browser.png
:width: 60%
:alt: The File Browser tab with a list of FITS files, the path box and its buttons

The **File Browser** tab with a file selected.
:::

#### Acquisition options

The button next to the *Enter image number* box opens the acquisition options.
They change how the **next** acquisition you start is set up:

**Manual acquisition type**
: Always open the [Select Acquisition Type dialog](#select-acquisition-type-dialog), instead of letting
  Pygacq work out the type from the image. Use it when Pygacq picks the wrong
  type.

**Clean NIR image**
: Clean the near-infrared acquisition image before it is used. Not available yet: the option can't be ticked.

**Create coo file from MOS image**
: Instead of acquiring, mark the alignment boxes on a MOS mask-in image by
  hand, to create the coordinates file for a mask that has no MDF. The image
  must have the MOS mask in the beam.

:::{figure} images/acquisition-options.png
:width: 60%
:alt: The acquisition options panel opened from the button next to the image number box

The acquisition options, opened from the button next to the *Enter image
number* box.
:::

:::{note}
Tick the options **before** you start the acquisition: an option ticked while
an acquisition is running doesn't affect it. The options are cleared when the
acquisition ends or is aborted, so they never carry over to the next one.
:::

#### Choosing the slit and sky images yourself

With **Auto** selected (the default), Pygacq finds the slit and sky images
among the images of the observation. This is what you want in most cases.
To use a different image, e.g. because the automatic sky image has a star in
the wrong place, select **User** for **Slit** or **Sky**, and then either:

- tick the image's **Slit** or **Sky** box in the **Acquisitions**
  list; or
- type the image number (or click **Browse**) and click **Apply slit** or
  **Apply sky**.

:::{figure} images/user-sky-slit.png
:width: 60%
:alt: Slit and Sky set to User, with the slit and sky images ticked in the Acquisitions list

**Slit** and **Sky** set to **User**, with the slit and sky images ticked in
the list.
:::

The new image is used straight away, also in the middle of an acquisition.
Pygacq checks that the image is suitable. A slit image, for instance, has to be
taken with the slit in the beam and with the same instrument. If it isn't,
Pygacq shows a warning and keeps the old image.

In **Auto** mode the **Slit** and **Sky** boxes only show which images are being
used; you can't change them.

:::{note}
**Slit** and **MDF** can't both be set to **User** at the same time.
:::

### Current Acquisition

:::{important}
**Current Acquisition** is the part of the window you work with during an
acquisition. It changes at every step: it tells you what Pygacq has found, what
to check, and what to do next, and it waits for you to act. Keep an eye on it
until the acquisition is finished.
:::

The **Current Acquisition** tab takes you through the acquisition one step at a
time. When no acquisition is running it shows *No Ongoing Acquisition*; while an
acquisition starts it shows *Loading acquisition image…* and then *Processing
acquisition image…*. From then on it has these parts, from top to bottom:

**Title and flags**
: The type of acquisition, e.g. **GMOS Longslit Acquisition**. Flags next to
  it point out special cases, such as **Two targets**, **Blind Offset** or
  **Off-axis**.

**Step buttons**
: One button per step, e.g. **Mark target(s)**, **Confirm slit center** and
  **Send offsets** for long-slit. The current step is blue and finished steps
  get a tick. Click the button of an earlier step to go back to it.

**Status box**
: A coloured box naming the current step or its result, e.g. **MARK
  TARGET(S)**, **SLIT AUTO-TRACING COMPLETED** or **SLIT AUTO-DETECTION
  FAILED**, with a short message on what to check or do. It also tells you when
  Pygacq reuses an earlier measurement, e.g. *Reusing previous slit measurement
  from …*.

**Choices and buttons**
: What you can decide in this step. For example, when marking the target you
  choose **One-target acquisition** or **Two-target acquisition** and click
  **Accept**; when checking the slit you click **Accept slit position** or
  **Remeasure slit**, or use **Use default slit position** or **Use previous
  slit measurement**. Pressing {kbd}`Q` or {kbd}`Enter` in the image does the
  same as the highlighted button.

**Instructions**
: The keys you can use in the image for this step, e.g. {kbd}`R` or {kbd}`X`
  to mark the target, or {kbd}`T` to trace the slit.

**Use custom acquiring position**
: An advanced section, closed by default, to acquire at a position other than
  the nominal one: enter X and Y, or click **Mark in image** and click the
  position, then **Apply**. **Reset** goes back to the initial nominal position.

When the measurements are done, the tab shows the offsets:

- The grey text under **CALCULATED OFFSETS** gives the reason for the advice:
  which limit the offsets are above or below, e.g. *\|P\| > 10% of the slit
  width*. It turns red when it is a warning.
- The button that matches the **OFFSET ADVICE** is highlighted, so {kbd}`Q` or
  {kbd}`Enter` follows the advice.

:::{figure} images/offsets-page.png
:width: 50%
:alt: The offsets page of a GMOS long-slit acquisition, with the grey reason under the offsets and Send offsets to telescope highlighted

The offsets page: the grey text gives the reason for the advice, and the
button that follows the advice is highlighted.
:::

After you send or ignore the offsets, the acquisition is over: you can no
longer go back to earlier steps. Follow the **NEXT STEP** advice, e.g. take
another acquisition image or start the science sequence. **Copy Offsets**
copies the offsets to the clipboard, e.g. for the night log.

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
