namespace alertApp
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            lblResult = new Label();
            lblStatus = new Label();
            lblZone1 = new Label();
            lblZone2 = new Label();
            lblZone3 = new Label();
            SuspendLayout();
            // 
            // lblResult
            // 
            lblResult.BorderStyle = BorderStyle.FixedSingle;
            lblResult.Font = new Font("Segoe UI", 11F, FontStyle.Bold, GraphicsUnit.Point);
            lblResult.ForeColor = Color.Black;
            lblResult.Location = new Point(176, 312);
            lblResult.Name = "lblResult";
            lblResult.Size = new Size(413, 71);
            lblResult.TabIndex = 4;
            // 
            // lblStatus
            // 
            lblStatus.BackColor = Color.Red;
            lblStatus.BorderStyle = BorderStyle.FixedSingle;
            lblStatus.Font = new Font("Segoe UI", 12F, FontStyle.Bold, GraphicsUnit.Point);
            lblStatus.Location = new Point(268, 41);
            lblStatus.Name = "lblStatus";
            lblStatus.Size = new Size(218, 38);
            lblStatus.TabIndex = 5;
            lblStatus.Text = "Off";
            lblStatus.TextAlign = ContentAlignment.MiddleCenter;
            // 
            // lblZone1
            // 
            lblZone1.BackColor = Color.Red;
            lblZone1.BorderStyle = BorderStyle.FixedSingle;
            lblZone1.Font = new Font("Segoe UI", 12F, FontStyle.Bold, GraphicsUnit.Point);
            lblZone1.Location = new Point(146, 146);
            lblZone1.Name = "lblZone1";
            lblZone1.Size = new Size(113, 38);
            lblZone1.TabIndex = 6;
            lblZone1.Text = "Zone 1";
            lblZone1.TextAlign = ContentAlignment.MiddleCenter;
            // 
            // lblZone2
            // 
            lblZone2.BackColor = Color.Red;
            lblZone2.BorderStyle = BorderStyle.FixedSingle;
            lblZone2.Font = new Font("Segoe UI", 12F, FontStyle.Bold, GraphicsUnit.Point);
            lblZone2.Location = new Point(318, 146);
            lblZone2.Name = "lblZone2";
            lblZone2.Size = new Size(113, 38);
            lblZone2.TabIndex = 7;
            lblZone2.Text = "Zone 2";
            lblZone2.TextAlign = ContentAlignment.MiddleCenter;
            // 
            // lblZone3
            // 
            lblZone3.BackColor = Color.Red;
            lblZone3.BorderStyle = BorderStyle.FixedSingle;
            lblZone3.Font = new Font("Segoe UI", 12F, FontStyle.Bold, GraphicsUnit.Point);
            lblZone3.Location = new Point(509, 146);
            lblZone3.Name = "lblZone3";
            lblZone3.Size = new Size(113, 38);
            lblZone3.TabIndex = 8;
            lblZone3.Text = "Zone 3";
            lblZone3.TextAlign = ContentAlignment.MiddleCenter;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(9F, 21F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(800, 450);
            Controls.Add(lblZone3);
            Controls.Add(lblZone2);
            Controls.Add(lblZone1);
            Controls.Add(lblStatus);
            Controls.Add(lblResult);
            Name = "Form1";
            Text = "Form1";
            ResumeLayout(false);
        }

        #endregion
        private Label lblResult;
        private Label lblStatus;
        private Label lblZone1;
        private Label lblZone2;
        private Label lblZone3;
    }
}