# F2 two-target acquisition (faint target)

This example is a Flamingos-2 long-slit acquisition of a faint target, Target1
(GS-2026A-Q-311-36), in the H band with the 6-pixel slit. Two objects are placed
on the slit at once, so Pygacq also calculates a rotation. It uses five images:

| Image            | What it is                   | Slit in beam | P (") | Q (") |
|------------------|------------------------------|--------------|-------|-------|
| S20260502S0065   | Sky image                    | no           | 0.0   | 10.0  |
| S20260502S0066   | Field image                  | no           | 0.0   | 0.0   |
| S20260502S0067   | Off-target slit image        | yes          | 10.0  | 0.0   |
| S20260502S0068   | Through-slit sky image       | yes          | 0.0   | 10.0  |
| S20260502S0069   | Through-slit on-target image | yes          | 0.2   | 0.0   |

The target is too faint to see well against the near-infrared sky, so each
acquisition image has a sky image taken 10" away in Q. Pygacq looks for it among
the previous images and subtracts it, which makes the target stand out. The sky
image is ticked in the **Sky** column of the **Acquisitions** list.

## 1. Load the field image and its sky image

Type `S20260502S0066` in the *Enter image number* box and press {kbd}`Enter`.

Pygacq subtracts the sky image, `S20260502S0065`, and measures the slit center on
the off-target slit image, `S20260502S0067`. Check the ticks in the **Sky** and
**Slit** columns.

<!-- TODO: screenshot of the Acquisitions list with the Sky and Slit ticks. -->

## 2. Mark the two targets

Select **Two-target acquisition**. The title of the **Current Acquisition** tab
gets a **Two targets** flag.

Put the cursor on the first target and press {kbd}`R`, then click **Accept First
Target**. Mark the second target the same way and click **Accept Second Target**.

<!-- TODO: say which object to mark first, and add a screenshot of the
     sky-subtracted field image with both targets marked. -->

## 3. Confirm the slit center

Check and accept the slit measurement on `S20260502S0067`, as in
[the GMOS example](longslit-gmos.md#4-confirm-the-slit-center).

## 4. Send the offsets and take the through-slit image

The offsets now include a rotation, **Rot**. The advice is to apply the offsets
and take the through-slit image. To follow it, press {kbd}`Enter`.

## 5. Load the through-slit image

Type `S20260502S0069` in the *Enter image number* box and press {kbd}`Enter`.
Pygacq subtracts the through-slit sky image, `S20260502S0068`.

Mark both targets again, as in [step 2](#2-mark-the-two-targets).

<!-- TODO: check whether Pygacq reuses the slit measurement here or asks to
     confirm the slit center, and add a screenshot of the sky-subtracted
     through-slit image with both targets marked. -->

## 6. Read the offset advice

With two targets, Pygacq adds the shift that the rotation causes at the targets
to \|P\|. The advice is to take another acquisition image if \|P\| plus that shift
is above 10% of the slit width, or \|Q\| is above 0.5". Otherwise it is to ignore
the offsets and start science.

<!-- TODO: add the offsets and advice for S20260502S0069, what the observer
     did, and a screenshot of the offsets page. -->
