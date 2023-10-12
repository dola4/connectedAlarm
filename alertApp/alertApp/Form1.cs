using MySql.Data.MySqlClient;
using System;
using System.Net.Http;
using System.Text.Json;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace alertApp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            InitializeTimer();
        }

        private void InitializeTimer()
        {
            System.Windows.Forms.Timer timer = new System.Windows.Forms.Timer();
            timer.Interval = 3000; 
            timer.Tick += async (s, e) =>
            {
                Alarm alarmData = await GetDataAsync();
                UpdateLabels(alarmData);
            };
            timer.Start();
        }

        private async Task<Alarm> GetDataAsync()
        {
            using (var httpClient = new HttpClient())
            {
                string url = "http://192.168.126.1:63712/HomeController/SendData?id=1";
                var response = await httpClient.GetAsync(url);
                response.EnsureSuccessStatusCode();
                string content = await response.Content.ReadAsStringAsync();
                Alarm alarmData = JsonSerializer.Deserialize<Alarm>(content);
                return alarmData;
            }
        }

        private void UpdateLabels(Alarm alarmData)
        {
            if (alarmData.status == 1)
            {
                lblStatus.BackColor = Color.Red;
                lblStatus.Text = "System Armed";
                if (alarmData.zone == "zone1")
                {
                    lblZone1.BackColor = Color.Red;
                }
                if (alarmData.zone == "zone2")
                {
                    lblZone2.BackColor = Color.Red;
                }
                if (alarmData.zone == "zone3")
                {
                    lblZone3.BackColor = Color.Red;
                }
                lblResult.Text = "System State : Armed \n" +
                                "Piece : " + alarmData.zone + "\n " +
                                "Moment : " + alarmData.moment;
            }
            else
            {
                lblStatus.BackColor = lblZone1.BackColor = lblZone2.BackColor = lblZone3.BackColor = Color.Green;
                lblResult.Text = "System State : Alarm Off \n" +
                                "Piece : " + alarmData.zone + "\n " +
                                "Moment : " + alarmData.moment;
            }
        }
    }

    public class Alarm
    {
        public int id { get; set; }
        public int status { get; set; }
        public string zone { get; set; }
        public DateTime moment { get; set; }
    }
}
