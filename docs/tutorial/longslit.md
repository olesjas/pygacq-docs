# Long-slit acquisition

This example is a GMOS-S long-slit acquisition of a relatively bright target 2026sfn
(GS-2026A-Q-122-40). It uses four images:

| Image            | What it is                   | Slit in beam | P (") | Q (") |
|------------------|------------------------------|--------------|-------|-------|
| S20260713S0077   | Field image                  | no           | 0.0   | 0.0   |
| S20260713S0078   | Off-target slit image        | yes          | 10.0  | 0.0   |
| S20260713S0079   | Through-slit on-target image | yes          | −3.1  | 0.1   |
| S20260713S0080   | Through-slit on-target image | yes          | −3.0  | 0.1   |

P and Q are the telescope offsets of each image.

The observer took the first two images, then started
the acquisition on the zero-offset field image.

## 1. Load the field image

Type `S20260713S0077` in the *Enter image number* box and press {kbd}`Enter`.

Pygacq finds the slit image of this observation and measures the slit center
on it. The **Slit** column of the **Acquisitions** list shows which image it
picked. To use a different one, see
[Choosing the slit and sky images yourself](main-window.md#choosing-the-slit-and-sky-images-yourself).

:::{figure} images/ls-acquisitions-list-with-arrows.png
:width: 60%
:alt: The Acquisitions list with the field image loaded and its associated slit image ticked

The associated slit image is ticked in the **Slit** column.
:::

## 2. Find the target with the finder chart

Pygacq found a finder chart named after the target and shows it in the **Finder
Charts** tab. To enlarge it, click the expand button below the chart.

The chart has North up and East left. To orient the acquisition image the same
way, click ![](images/icons/orient_ne.svg){w=22px} in the toolbar under the
image (see
[Changing the image orientation](getting-started.md#changing-the-image-orientation)).

:::{figure} images/ls-finder-chart-with-arrows.png
:width: 100%
:alt: The finder chart next to the acquisition image oriented North up and East left

The finder chart and the acquisition image, both North up and East left.
:::

## 3. Mark the target

From here on, the **Current Acquisition** tab guides you step by step. Read it
at every step.

Pygacq displays the acquisition image with the slit overlay where the slit is
expected, and a pink cross where the target has to end up. In this example, the target is the star closest to the cross.

Leave **One-target acquisition** selected, put the cursor on the star and press
{kbd}`R`. Pygacq centroids the star and marks it. Check the fit in the
**Analysis** tab, then click **Accept** or press {kbd}`Q`.

:::{figure} images/ls-mark-target-with-arrows.png
:width: 100%
:alt: The marked target, with the current step, its instructions and One-target acquisition highlighted in the Current Acquisition tab

The marked target. The **Current Acquisition** tab shows the current step, its
instructions, and **One-target acquisition** selected.
:::

## 4. Confirm the slit center

Pygacq traces the slit on the off-target slit image, `S20260713S0078`, and
switches the viewer to it, with the measured center and the slit overlay drawn
on it. The plot in the **Analysis** tab shows the slit center measured along the
slit.

Check that the overlay lies along the slit. To see the slit without it, click
**Hide slit overlay**.

If the measurement is right, click **Accept slit position** or press {kbd}`Q`.
Otherwise click **Remeasure slit** and measure it yourself.

:::{note}
If tracing fails, or you click **Remeasure slit**, the tab shows instructions
for marking the slit center yourself: press {kbd}`T` inside the slit to trace
it, or {kbd}`J` ({kbd}`K` for a horizontal slit) to find its center from a
cross-cut.
:::

:::{figure} images/ls-confirm-slit-with-arrows.png
:width: 100%
:alt: The Confirm slit center step: the traced slit on the slit image and the slit-tracing plot in the Analysis tab

The traced slit on `S20260713S0078`, and the slit-tracing plot on the left.
:::

## 5. Send the offsets

The advice is to apply the offsets and take the through-slit image. To follow
it, press {kbd}`Enter`.

That ends this pass of the acquisition: you can no longer go back to earlier
steps. The last page says what to do next under **NEXT STEP**. 

At night, you
would now take the next image of the acquisition sequence, the through-slit
on-target image. **Copy Offsets** copies the offsets, e.g. for the OT.

## 6. Load the through-slit image

Type `S20260713S0079` in the *Enter image number* box and press {kbd}`Enter`.

The slit is in the beam now, so this image is ticked in the **Slit** column of
the **Acquisitions** list and could be used to measure the slit itself. The GMOS slit position is stable, so Pygacq reuses the measurement from
the off-target slit image instead and says so on the target-marking page:
*Reusing previous slit measurement from S20260713S0078*.

Check that the slit overlay from that measurement still lies along the slit.

:::{figure} images/ls-reuse-message-with-arrows.png
:width: 50%
:alt: The Mark target(s) step with the message that the previous slit measurement is reused

Pygacq reuses the slit measurement from `S20260713S0078`.
:::

## 7. Mark the target in the slit

Mark the target as in [step 3](#3-mark-the-target). The slit cuts off part of
the star, so the {kbd}`R` fit may be poor. If it is, press {kbd}`X` on the center
of the star in the contour plot. Accept with {kbd}`Q`.

:::{figure} images/ls-target-in-slit.png
:width: 50%
:alt: The contour plot of the target in the slit

The contour plot of the target in the slit. Press {kbd}`X` on the center of the star.
:::

:::{note}
The **Confirm slit center** step is skipped here, because the slit measurement
is reused. To measure the slit on this image instead, click **Accept target,
remeasure slit**, or click the **Confirm slit center** step button to go back
to it.
:::

## 8. Send the offsets to improve the centering

The offsets are small, so Pygacq advises *Ignore offsets and start science
immediately*. The grey text under the offsets says why: *\|P\| < 10% of the slit
width and \|Q\| < 0.5"*.

During the actual observation, the observer chose to improve the centering and
sent the offsets anyway. To do the same, click **Send offsets to telescope**.
Don't press {kbd}`Enter`: the highlighted button follows the advice and ignores
the offsets.

After the offsets were applied, another through-slit on-target image was taken.

:::{figure} images/ls-offsets-ignore.png
:width: 60%
:alt: The offsets page advising to ignore the offsets, with Ignore offsets highlighted

The offsets are small, and **Ignore offsets** is highlighted.
:::

## 9. Check the centering and start science

Load the next through-slit image, `S20260713S0080`, and repeat
[steps 6](#6-load-the-through-slit-image) and [7](#7-mark-the-target-in-the-slit).
The slit measurement is reused again, so the **Confirm slit center** step is
skipped.

The target is now well centered in the slit, and Pygacq advises *Ignore offsets
and start science immediately*. To follow the advice, press {kbd}`Enter`. The
last page says to start the science sequence.
