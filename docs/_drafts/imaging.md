# Imaging acquisition

This example is a GMOS imaging acquisition. In imaging there is no slit, fiber
bundle or keyhole to measure: you only mark the target.

<!-- TODO: add the image number of this example (see the EXAMPLES file). -->

## 1. Load the acquisition image

Type the image number in the *Enter image number* box and press {kbd}`Enter`.

## 2. Choose the acquisition type

If the **Select Acquisition Type** dialog opens, choose **Imaging** and click
**Select**.

## 3. Mark the target

The acquisition image is shown with the nominal position marked, and the **Current Acquisition**
tab switches to the **Mark target** step. Move the cursor over the target in the
**Acquisition Image** and press one of:

{kbd}`R`
: Calculate the centroid of the star under the cursor and mark it. This is the
  usual choice. The radial profile appears in the **Analysis** tab so you can
  check the fit.

{kbd}`X`
: Mark exactly the position under the cursor, without fitting. Use this for
  targets that can't be centroided, e.g. extended objects. You can also press
  {kbd}`X` on the contour plot in the **Analysis** tab.

You can mark the target again as often as you like; the last mark is the one
used.

When you are happy with the position, click **Accept** or press {kbd}`Q`.

:::{note}
By default the target is placed at the nominal position, the rotation center.
To acquire at a different position, open **Use custom acquiring position** on
the same page, enter the X and Y pixel coordinates (or click **Mark in image**
and click the position in the image), then click **Apply**. **Reset** goes
back to the nominal position.
:::

## 4. Send the offsets

Pygacq calculates the offsets that move the target from where you marked it to
where it should be, and shows them under **CALCULATED OFFSETS**:

```text
P = -3.124", Q = 1.096"
```

The **OFFSET ADVICE** box says what to do next, based on how large the offsets
are compared with the size of the imaging field:

| Offsets                        | Advice                                              |
|--------------------------------|-----------------------------------------------------|
| larger than 10% of the field   | Apply offsets and take another acquisition image.   |
| between 1% and 10% of the field| Apply offsets and start science immediately.        |
| smaller than 1% of the field   | Ignore offsets and start science immediately.       |

The line under the offsets (e.g. *\|P\| > 1% of imaging field size*) tells you
which case applies. Click **Send offsets to telescope** or **Ignore offsets**,
or press {kbd}`Enter` to follow the advice.

:::{note}
For a blind offset the limits are tighter: offsets larger than 1% of the field
are sent and followed by another acquisition image. Smaller offsets are
ignored, and Pygacq reminds you to move the telescope back to the base
position and to start science once guiding has been restored.
:::

## 5. Finish

The last page shows the offsets and the next step: *Start the science
sequence*, or *Take another acquisition image*. In the second case, take the
image and start again from [step 1](#1-load-the-acquisition-image).
