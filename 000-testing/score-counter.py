august = [
	624.50, 676.18, 617.89,	633.62, 721.52,
	653.03, 631.70, 710.47, 763.29, 687.29,
	682.21, 672.89, 695.76, 645.97, 623.81,
	658.33, 677.64, 630.22
]

september = [
	650.56, 603.71, 692.17, 620.25, 714.77,
	699.48, 635.54, 670.59, 649.61, 656.15,
	605.54, 698.53, 696.67, 644.67, 786.60,
	666.03, 618.24, 597.87, 647.30, 679.90,
	722.68, 803.32, 718.50, 676.91, 656.69,
	682.21, 663.56, 686.23, 669.25
]

targets_amount = len(august + september)
score = sum(august + september)
score_avg = score / targets_amount

print("Targets registered: {}\nScore: {:.2f}\nAverage score: {:.2f}".format(targets_amount, score, score_avg))