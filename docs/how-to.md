# How to

Short answers to common tasks. For the full description of each part of the
window, see [The main window in detail](tutorial/main-window.md).

## Do a two-target acquisition

At the **Mark target(s)** step, select **Two-target
acquisition** in the **Current Acquisition** panel. Mark the first target with {kbd}`R` and click **Accept First
Target**, then mark the second target and click **Accept Second Target**.

## Do an off-axis acquisition

Long-slit only, GMOS and F2. The target stays where it is along the slit, and is
centered only across it. To set this up:

At the **Confirm slit center** step, open **Use custom acquiring position** at
the bottom of the panel, and tick **Use target's Y-coordinate**
(**X-coordinate** for a horizontal slit).

The **Off-axis** flag then appears in the panel title, and the Q offset stays
zero.

## Run an acquisition on an older image

If the image is no longer in dataflow, download it from
[archive.gemini.edu](https://archive.gemini.edu) and put it in the user data
directory. Put its associated images there too, e.g. the slit image or the MDF,
and Pygacq finds them as well.

During the testing period the user data directory is
`~/Scratch/pygacq_test/user_data`. After that, use the Pygacq cache directory
instead.

## Align the acquisition image North up, East left

Click ![](tutorial/images/icons/orient_ne.svg){w=22px} button in
the toolbar under the acquisition image. **Reset**
(![](tutorial/images/icons/reset_rotation.svg){w=22px}) undoes it. See
[Changing the image orientation](tutorial/getting-started.md#changing-the-image-orientation).

## Measure distances

Click ![](tutorial/images/icons/ruler.svg){w=22px} **Ruler** in the toolbar and
drag between two points in the image. 


## Create a coordinate file from a MOS mask-in image

This creates a coordinates file from an image with the MOS mask in the beam, for
a mask whose MDF is missing or bad.

1. Click the three-dots button next to the *Enter image number* box and tick
   **Create coo file from MOS image**.
2. Load the mask-in image.
3. Mark the alignment boxes, following the **Current Acquisition** tab.

Pygacq saves the coordinates file in three places and shows the paths. **Copy
coordinate file name** copies its name.

[Acquisition options](tutorial/main-window.md#acquisition-options).

## Run a MOS acquisition with a coordinate file

Use a coordinate file instead of an MDF, e.g. one you created from a mask-in
image. It is a text file with the box positions, one `x y` pair per line.

Before starting the acquisition, set **MDF** to **User**. Type just the file
name if the file is in the program folder or in the Pygacq user data directory
(the cache directory after the testing period), or the full path if it is
somewhere else. You can also click **Browse** to find it. Then click **Apply
MDF**.

## Choose the slit and sky images yourself

Pygacq picks them from the images of the observation. To use different ones, set
**Slit** or **Sky** to **User**, then either tick the image's **Slit** or **Sky**
box in the **Acquisitions** list, or type its image number (or click **Browse**)
and click **Apply slit** or **Apply sky**.

This works during an acquisition too. Pygacq checks the image first, and keeps
the old one if it isn't suitable. See
[Choosing the slit and sky images yourself](tutorial/main-window.md#choosing-the-slit-and-sky-images-yourself).

## Run an acquisition without type auto-detection

Click the options button (three dots) next to the *Enter image number* box and tick **Manual
acquisition type**, then load the image. Pygacq opens the **Select Acquisition
Type** dialog instead of working out the type itself.

The option only applies to the next acquisition you start. See
[Select Acquisition Type dialog](tutorial/main-window.md#select-acquisition-type-dialog).

## Not reuse previous measurements

Pygacq keeps earlier measurements, such as the slit position, in its database
and reuses them in later acquisitions of the same observation. To measure
everything from scratch, tick **Don't reuse previous measurements** in the
acquisition options, under the three-dots button next to the *Enter image
number* box, before starting the acquisition.

To remeasure only the slit in the current acquisition, click **Accept target,
remeasure slit** instead. For testing, **File → Cleanup → Reset Database**
clears the measurements of every observation. See
[Clearing the cache and the database](tutorial/getting-started.md#clearing-the-cache-and-the-database).

## See an image's header

Click the image in the **Acquisitions** list: its header appears in the **Image
Header** tab, and a summary in the **Image Info** tab. To find a keyword, type
it in the **Filter** box.

For the image in the viewer, just open the **Image Header** tab. See
[Image Header and Image Info](tutorial/main-window.md#image-header-and-image-info).

## Look at another image

Click folder icon above the viewer tabs and choose a FITS file.
It opens in the **Other Image** tab, where the analysis keys work too.

To compare it with the acquisition image, use **Match**, **Grid View** or
**Blink Frames**. See
[Looking at another image](tutorial/main-window.md#looking-at-another-image).
