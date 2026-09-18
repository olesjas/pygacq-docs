# GMOS long-slit acquisition

This example is a GMOS-S long-slit acquisition of a relatively bright supernova
(GS-2024B-Q-417-201). It uses four images:

| Image            | What it is                   | Slit in beam | P (") | Q (") |
|------------------|------------------------------|--------------|-------|-------|
| S20250115S0279   | Field image                  | no           | 0.0   | 0.0   |
| S20250115S0280   | Off-target slit image        | yes          | 10.0  | 0.0   |
| S20250115S0281   | Through-slit on-target image | yes          | −0.4  | −0.6  |
| S20250115S0282   | Through-slit on-target image | yes          | −0.3  | −0.6  |

P and Q are the telescope offsets of each image.

The observer took the first (field) images, then started
the acquisition on it while the second image was still exposing.

:::{tip}
You don't have to wait for the slit image to finish. Start the acquisition as
soon as the field image is available: Pygacq picks up the slit image when it
arrives.
:::

## 1. Load the field image

Type `S20250115S0279` in the *Enter image number* box and press {kbd}`Enter`.

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

This target has a finder chart, but its file name doesn't contain the full
target name, so Pygacq didn't match it. The **Finder Charts** tab shows the list
of all charts in the program directory instead, with the target name at the top.
Find the chart whose name contains it and double-click it to open it. To enlarge
it, click the expand button below the chart.

:::{figure} images/ls-finder-chart-list-with-arrows.png
:width: 60%
:alt: The Finder Charts tab listing the charts of the program, with the target name at the top

The target name, `SN 2024ggi`, and the charts found in the program directory.
Its chart is named `2024ggi_colored.png`.
:::

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

Pygacq traces the slit on the off-target slit image, `S20250115S0280`, and
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

The traced slit on `S20250115S0280`, and the slit-tracing plot on the left.
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

Type `S20250115S0281` in the *Enter image number* box and press {kbd}`Enter`.

The slit is in the beam now, so this image is ticked in the **Slit** column of
the **Acquisitions** list and could be used to measure the slit itself. The GMOS slit position is stable, so Pygacq reuses the measurement from
the off-target slit image instead and says so on the target-marking page:
*Reusing previous slit measurement from S20250115S0280*.

Check that the slit overlay from that measurement still lies along the slit.

:::{figure} images/ls-reuse-message-with-arrows.png
:width: 50%
:alt: The Mark target(s) step with the message that the previous slit measurement is reused

Pygacq reuses the slit measurement from `S20250115S0280`.
:::

## 7. Mark the target in the slit

Mark the target as in [step 3](#3-mark-the-target). It is bright and not cut by
the slit, so {kbd}`R` centroids it well. Accept with {kbd}`Q`.

:::{figure} images/ls-target-in-slit-with-arrows.png
:width: 100%
:alt: The second pass: the target marked in the slit on the through-slit image

The target marked in the slit on the through-slit image.
:::

:::{tip}
If the slit cuts off part of the target, the {kbd}`R` fit can land off center.
You can mark the star with {kbd}`X` in the contour plot instead.
:::

:::{note}
The **Confirm slit center** step is skipped here, because the slit measurement
is reused. To measure the slit on this image instead, click **Accept target,
remeasure slit**, or click the **Confirm slit center** step button to go back
to it.
:::

## 8. Send the offsets to improve the centering

The offsets are P = 0.105", Q = 0.037". \|P\| is just over 10% of the slit
width, so the advice is to apply them and take another acquisition image. To
follow it, press {kbd}`Enter`.

After the offsets were applied, another through-slit on-target image was taken.

<!-- TODO: screenshot of the offsets page for S20250115S0281. -->

## 9. Check the centering and start science

Load the next through-slit image, `S20250115S0282`, and repeat
[steps 6](#6-load-the-through-slit-image) and [7](#7-mark-the-target-in-the-slit).
The slit measurement is reused again, so the **Confirm slit center** step is
skipped.

The target is now well centered in the slit: the offsets are P = −0.005",
Q = 0.045", both within the limits, so the advice is to ignore them and start
science. To follow it, press {kbd}`Enter`. The last page says to start the
science sequence.

:::{figure} images/ls-offsets-ignore.png
:width: 60%
:alt: The offsets page advising to ignore the offsets, with Ignore offsets highlighted

The offsets are small, and **Ignore offsets** is highlighted.
:::
