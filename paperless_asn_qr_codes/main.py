import argparse

from reportlab.lib.units import mm, cm
from reportlab_qrcode import QRCodeImage
from paperless_asn_qr_codes import avery_labels

def render(c,x,y):
    global startASN
    barcode_value = f"ASN{startASN:07d}"
    startASN = startASN + 1
    
    qr = QRCodeImage(barcode_value, size=y*0.9)
    qr.drawOn(c,1*mm,y*0.05)
    c.setFont("Helvetica", 2*mm)
    c.drawString(y, (y-2*mm)/2, barcode_value)

def main():
    parser = argparse.ArgumentParser(
                    prog='paperless-asn-qr-codes',
                    description='CLI Tool for generating paperless ASN labels with QR codes')
    parser.add_argument('start_asn')
    parser.add_argument('output_file')
    args = parser.parse_args()
    global startASN
    startASN = int(args.start_asn)
    label = avery_labels.AveryLabel(4731)
    label.open(args.output_file)
    label.render(render, 189 )
    label.close()
