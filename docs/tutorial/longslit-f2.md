# F2 long-slit acquisition

This example is a Flamingos-2 long-slit acquisition of a faint target,
so sky subtraction is used (GS-2025A-Q-420-75). It uses five images:

| Image            | What it is                     | Slit in beam | P (") | Q (") |
|------------------|--------------------------------|--------------|-------|-------|
| S20250611S0050   | Sky for the field image        | no           | 0.0   | 10.0  |
| S20250611S0051   | Field image                    | no           | 0.0   | 0.0   |
| S20250611S0052   | Off-target slit image          | yes          | 10.0  | 0.0   |
| S20250611S0053   | Sky for the through-slit image | yes          | −0.4  | 14.3  |
| S20250611S0054   | Through-slit on-target image   | yes          | −0.4  | 4.3   |

P and Q are the telescope offsets of each image. The observer took the first two images
(the sky and the field image) and started the acquisition while the off-target slit image
was slit exposing.

:::{tip}
You don't have to wait for the slit image to finish. Start the acquisition as
soon as the field image is available: Pygacq picks up the slit image when it
arrives.
:::

## 1. Load the field image

Type `S20250611S0051` in the *Enter image number* box and press {kbd}`Enter`.
Pygacq finds and subtracts the sky image, `S20250611S0050`.

Pygacq also finds the slit image of this observation and measures the slit
center on it. The **Slit** and **Sky** columns of the **Acquisitions** list show
which images it picked. To use different ones, see
[Choosing the slit and sky images yourself](main-window.md#choosing-the-slit-and-sky-images-yourself).

:::{figure} images/ls-f2-acquisitions-list.png
:width: 60%
:alt: The Acquisitions list with the sky image ticked in the Sky column and the slit image in the Slit column

The sky image, `S20250611S0050`, is ticked in the **Sky** column, and the slit
image, `S20250611S0052`, in the **Slit** column.
:::

## 2. Find the target with the finder chart

Pygacq found a finder chart named after the target and shows it in the **Finder
Charts** tab. To enlarge it, click the expand button below the chart.

The chart has North up and East left. To orient the acquisition image the same
way, click ![](images/icons/orient_ne.svg){w=22px} in the toolbar under the
image (see
[Changing the image orientation](getting-started.md#changing-the-image-orientation)).

:::{figure} images/ls-f2-finder-chart.png
:width: 100%
:alt: The finder chart next to the sky-subtracted field image, both North up and East left

The finder chart and the sky-subtracted field image, both North up and East
left.
:::

## 3. Mark the target

From here on, the **Current Acquisition** tab guides you step by step. Read it
at every step.

Pygacq displays the acquisition image with the slit overlay where the slit is
expected, and a pink cross where the target has to end up.

Leave **One-target acquisition** selected, put the cursor on the target and
press {kbd}`R`. Pygacq centroids it and marks it. Check the fit in the
**Analysis** tab, then click **Accept** or press {kbd}`Q`.

:::{figure} images/ls-f2-mark-target.png
:width: 100%
:alt: The target marked on the sky-subtracted field image, with the fit in the Analysis tab

The marked target on the sky-subtracted field image, with its fit in the
**Analysis** tab.
:::

## 4. Confirm the slit center

Pygacq traces the slit on the off-target slit image, `S20250611S0052`, and
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
it, or {kbd}`K` to find its center from a cross-cut.
:::

:::{figure} images/ls-f2-confirm-slit.png
:width: 100%
:alt: The Confirm slit center step: the traced slit on S20250611S0052 and the slit-tracing plot in the Analysis tab

The traced slit on `S20250611S0052`, and the slit-tracing plot on the left.
:::

## 5. Send the offsets

The advice is to apply the offsets and take the through-slit image. To follow
it, press {kbd}`Enter`.

That ends this pass of the acquisition: you can no longer go back to earlier
steps. The last page says what to do next under **NEXT STEP**.

At night, you would now take the next two images of the acquisition sequence, the
sky image and the through-slit on-target image. **Copy Offsets** copies the
offsets, e.g. for the OT.

:::{figure} images/ls-f2-offsets.png
:width: 60%
:alt: The offsets page for S20250611S0051, advising to apply the offsets and take the through-slit image

The offsets for `S20250611S0051`: P = −0.279", Q = 4.268".
:::

## 6. Load the through-slit image

Type `S20250611S0054` in the *Enter image number* box and press {kbd}`Enter`.
Pygacq subtracts the sky image taken at the new position, `S20250611S0053`.

Pygacq reuses the measurement from the off-target slit image and says so on the
target-marking page: *Reusing previous slit measurement from S20250611S0052*.
That image stays ticked in the **Slit** column of the **Acquisitions** list,
because the measurement on screen is the one made on it.

Check that the slit overlay from that measurement still lies along the slit.

## 7. Mark the target in the slit

Mark the target as in [step 3](#3-mark-the-target) and accept with {kbd}`Q`.

:::{tip}
If the slit cuts off part of the target, the {kbd}`R` fit can land off center.
You can mark the target with {kbd}`X` in the contour plot instead.
:::

:::{note}
The **Confirm slit center** step is skipped here, because the slit measurement
is reused. To measure the slit on this image instead, click **Accept target,
remeasure slit**, or click the **Confirm slit center** step button to go back
to it.
:::

:::{figure} images/ls-f2-target-in-slit.png
:width: 100%
:alt: The target marked in the slit on the through-slit image, with the message that the previous slit measurement is reused

The target marked in the slit on `S20250611S0054`. The panel says *Reusing
previous slit measurement from S20250611S0052*, and `S20250611S0052` is ticked
in the **Slit** column.
:::

## 8. Check the centering and start science

The offsets are P = 0.014", Q = −0.089". \|P\| is compared with 10% of the slit
width, 0.072" here, and \|Q\| with 0.5". Both are within the limits, so the
advice is to ignore the offsets and start science. To follow it, press
{kbd}`Enter`.

:::{figure} images/ls-f2-offsets-ignore.png
:width: 60%
:alt: The offsets page for S20250611S0054, advising to ignore the offsets and start science

The offsets are small, and **Ignore offsets** is highlighted.
:::
