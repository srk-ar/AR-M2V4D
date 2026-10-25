# Cross section of the slope as a truncated shear wedge, in the parameters of
# the slope-period chapter: slope height Hs from the crest to the base, berm
# width b, base width bmax and slope ratio s (horizontal advance per unit of
# height). The extended slopes meet at the apex, H = Hs/(1 - lo) above the base
# and h = H - Hs = lo*H above the berm. The proportions are illustrative and no
# value is printed: the labels are symbols, so one drawing serves every
# language. Builds PLOT; GG_THEME comes from scripts/setup/setup.R.
PLOT <- local({
  LO <- 0.35    # truncation ratio of the drawing
  S <- 2        # slope ratio of the drawing
  HS <- 1       # slope height, the unit of the drawing
  GAP <- 0.35   # clearance between the section and its dimension lines
  NUDGE <- 0.08 # offset of a label from its line
  ApexHeight <- HS / (1 - LO)
  Toe <- S * ApexHeight          # half of the base width bmax
  Crest <- LO * Toe              # half of the berm width b
  Right <- Toe + GAP             # abscissa of the Hs and h dimension lines
  Outer <- Right + 2 * GAP       # abscissa of the H dimension line
  Below <- -GAP                  # ordinate of the bmax dimension line
  Inner <- HS - 0.4 * GAP        # ordinate of the b dimension line
  Step <- 0.62                   # ordinate of the slope-ratio triangle
  Leg <- 0.2                     # vertical leg of that triangle
  Corner <- Toe - S * Step       # where the triangle leaves the right slope
  Dimensions <- data.frame(
    x = c(-Crest, -Toe, Right, Right, Outer),
    y = c(Inner, Below, 0, HS, 0),
    xend = c(Crest, Toe, Right, Right, Outer),
    yend = c(Inner, Below, HS, ApexHeight, ApexHeight)
  )
  Witness <- data.frame(
    x = c(-Crest, Crest, -Toe, Toe, Crest, 0),
    y = c(HS, HS, 0, 0, HS, ApexHeight),
    xend = c(-Crest, Crest, -Toe, Toe, Right + GAP / 3, Outer + GAP / 3),
    yend = c(Inner - GAP / 3, Inner - GAP / 3, Below - GAP / 3, Below - GAP / 3, HS, ApexHeight)
  )
  Labels <- data.frame(
    x = c(0, 0, Right + NUDGE, Right + NUDGE, Outer + NUDGE, Corner + S * Leg / 2, Corner + S * Leg + NUDGE,
          -Toe, -Toe, -Toe),
    y = c(Inner - 2 * NUDGE, Below - 2 * NUDGE, HS / 2, (HS + ApexHeight) / 2, ApexHeight / 2, Step + NUDGE,
          Step - Leg / 2, ApexHeight - c(0, 3, 6) * NUDGE),
    label = c("b", "b[max]", "H[s]", "h", "H", "s", "1",
              "lambda[o] == b/b[max]", "H == H[s]/(1 - lambda[o])", "h == H - H[s] ~ '=' ~ lambda[o] ~ H"),
    hjust = c(0.5, 0.5, 0, 0, 0, 0.5, 0, 0, 0, 0)
  )
  ggplot2::ggplot() +
    ggplot2::annotate("segment", x = -Toe - GAP, y = 0, xend = Outer + GAP / 2, yend = 0,
                      linewidth = 0.6, colour = "grey15") +
    ggplot2::annotate("polygon", x = c(-Toe, Toe, Crest, -Crest), y = c(0, 0, HS, HS),
                      fill = "grey88", colour = "grey15", linewidth = 0.5) +
    ggplot2::annotate("segment", x = c(-Crest, Crest), y = HS, xend = 0, yend = ApexHeight,
                      linetype = "dashed", linewidth = 0.45, colour = "grey30") +
    ggplot2::annotate("point", x = 0, y = ApexHeight, size = 1.4, colour = "grey15") +
    ggplot2::annotate("path", x = c(Corner, Corner + S * Leg, Corner + S * Leg), y = c(Step, Step, Step - Leg),
                      linewidth = 0.4, colour = "grey15") +
    ggplot2::geom_segment(data = Witness, ggplot2::aes(x = x, y = y, xend = xend, yend = yend),
                          linetype = "dotted", linewidth = 0.3, colour = "grey45") +
    ggplot2::geom_segment(data = Dimensions, ggplot2::aes(x = x, y = y, xend = xend, yend = yend),
                          linewidth = 0.35, colour = "grey10",
                          arrow = ggplot2::arrow(length = ggplot2::unit(1.6, "mm"), ends = "both", type = "closed")) +
    ggplot2::geom_text(data = Labels, ggplot2::aes(x = x, y = y, label = label, hjust = hjust),
                       parse = TRUE, size = 3.6, colour = "grey10") +
    ggplot2::coord_equal(xlim = c(-Toe - GAP, Outer + 6 * NUDGE), ylim = c(Below - 4 * NUDGE, ApexHeight + 1.5 * NUDGE),
                         expand = FALSE) +
    GG_THEME +
    ggplot2::theme(
      axis.title = ggplot2::element_blank(), axis.text = ggplot2::element_blank(),
      axis.ticks = ggplot2::element_blank(), panel.grid = ggplot2::element_blank(),
      panel.border = ggplot2::element_blank(), panel.background = ggplot2::element_blank()
    )
})
